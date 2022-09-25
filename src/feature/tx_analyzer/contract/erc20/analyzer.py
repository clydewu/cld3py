# -*- coding: UTF-8 -*-
from flask import current_app as app
from web3.logs import IGNORE

from ....erc20_token.repository import ERC20TokenRepository
from ....transaction.repository import ReceiptLogRepository
from ....address.repository import AddressRepository, AddressTokenRepository
from ..base import BaseERCAnalyzer
from .const import ERC20_ABI, ERC20_NAME


class ERC20Analyzer(BaseERCAnalyzer):
    name = ERC20_NAME
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addr_to_token = {}
        tokens = ERC20TokenRepository.get_all()
        for token in tokens:
            token.contract = self.w3.eth.contract(token.address, abi=ERC20_ABI)
            self.addr_to_token[token.address] = token
        self.abi = ERC20_ABI

    def is_my_contract(self, address):
        return bool(self.addr_to_token.get(address))

    def analyze_log(self, receipt_log):        
        if not (token := self.addr_to_token.get(receipt_log.address)):
            token = ERC20TokenRepository.new(address=receipt_log.address)
            token.contract = self.w3.eth.contract(receipt_log.address, abi=ERC20_ABI)
        transfer = token.contract.events.Transfer().processLog(receipt_log)

        # if go to here, means this is a ERC20 token
        if transfer.get('args') and token.is_new():
            self._keep_token(token)

        from_addr = transfer.args['from']
        to_addr = transfer.args['to']
        value = transfer.args['value']
        app.logger.info(f'Get a Transfer event, token: {token.symbol}, from: {from_addr}, to: {to_addr}, value: {value}')

        try:
            from_address = self.crawler.get_address_balance(from_addr)
            from_addr_token = self.get_addr_token_balance(from_addr, token)
            to_address = self.crawler.get_address_balance(to_addr)
            to_addr_token = self.get_addr_token_balance(to_addr, token)
            receipt = ReceiptLogRepository.create(dict(
                transaction=self.w3.toHex(receipt_log.transactionHash),
                log_index=receipt_log.logIndex,
                address=receipt_log.address,
                block=self.w3.toHex(receipt_log.blockHash),
                token=token,
                from_addr=from_address,
                to_addr=to_address,
                value=value
            ))
        except Exception as err:
            app.logger.warn(f'{err}')
            raise err


    def _keep_token(self, token):
        token.name = token.contract.functions.name().call()
        token.symbol = token.contract.functions.symbol().call()
        token.decimals = token.contract.functions.decimals().call()
        ERC20TokenRepository.save(token)
        self.addr_to_token[token.address] = token

    def get_addr_token_balance(self, addr_str, token):
        if not (to_addr_token := AddressTokenRepository.get(addr_str, token)):
            app.logger.info(f'Get a address/token pair, create it, addr: {addr_str}, token: {token.name}')
            to_addr_token = AddressTokenRepository.create(dict(
                address=addr_str,
                token=token,
                balance=token.contract.functions.balanceOf(addr_str).call()
            ))
        return to_addr_token
        # to_addr_token.balance = token.contract.functions.balanceOf(addr_str).call()
        # AddressTokenRepository.save(to_addr_token)