# -*- coding: UTF-8 -*-

import json
from pprint import pprint
from flask import current_app as app, g
from web3.logs import IGNORE


from app_factory import scheduler

def main_job():
    with scheduler.app.app_context():
        # txn_hash = '0x8c41035a0af5b9db18c7328d9a13bd59b5404425cc3f9a8eae07459bb0f5a827'
        w3 = app.w3
        with open('./feature/erc20/erc20.abi.json') as fd:
            erc_20_abi = json.load(fd)
        # txn = app.w3.eth.get_transaction(txn_hash)

        target_block = w3.eth.get_block('latest')
        for txn in target_block.transactions:
            receipt = w3.eth.get_transaction_receipt(txn)
            # TODO, add native eth
            for event_log in receipt.logs:
                curr_erc20_contract = app.w3.eth.contract(event_log.address, abi=erc_20_abi)
                try:
                    results = curr_erc20_contract.events.Transfer().processReceipt(receipt, errors=IGNORE)
                    for result in results:
                        if not result.get('args'):
                            continue
                        args = result.args
                        app.logger.info(f'Get a Transfer event, from: {args["from"]}, to: {args["to"]}, value: {args["value"]}')
                except Exception as err:
                    app.logger.warning(f'Get non ERC20 address: {event_log.address}, err: {err}')
            
            
        app.logger.info(f'Resolved the latest block')