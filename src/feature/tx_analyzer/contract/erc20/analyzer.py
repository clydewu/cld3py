# -*- coding: UTF-8 -*-
from flask import current_app as app
from web3.logs import IGNORE

from ....erc20_token.repository import ERC20TokenRepository
from ..base import BaseERCAnalyzer
from .const import ERC20_ABI, ERC20_NAME


class ERC20Analyzer(BaseERCAnalyzer):
    name = ERC20_NAME
    
    def __init__(self):
        tokens = ERC20TokenRepository.get_all()
        self.addr_to_token = {t.address: t for t in tokens}
        self.addr_to_contract = {t.address: app.w3.eth.contract(t.address, abi=ERC20_ABI) for t in tokens}
        self.abi = ERC20_ABI

    def is_my_contract(self, address):
        return bool(self.addr_to_contract.get(address))

    def analyze_log(self, receipt_log):
        w3 = app.w3
        
        if contract := self.addr_to_contract.get(receipt_log.address):
            contract = w3.eth.contract(receipt_log.address, abi=ERC20_ABI)
        results = contract.events.Transfer().processLog(receipt_log)
        for result in results:
            if not result.get('args'):
                continue
            args = result.args
            app.logger.info(f'Get a Transfer event, from: {args["from"]}, to: {args["to"]}, value: {args["value"]}')

        if not self.is_my_contract(receipt_log.address):
            self.add_new_token_by_new_contract(contract)
            self.addr_to_contract[receipt_log.address] = contract

    def add_new_token_by_new_contract(self, contract):
        pass