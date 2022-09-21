# -*- coding: UTF-8 -*-

from flask import current_app as app

from app_factory import scheduler
from ..block.repository import BlockRepository
from ..transaction.repository import TransactionRepository
from .base import BaseCrawler


class BackwardCrawler(BaseCrawler):
    def start_crawler(self):
        with scheduler.app.app_context():
            target_height = self.w3.eth.block_number - 1
            while target_height > 0:
                try:
                    if the_lowest_block := BlockRepository.get_the_lowest_block():
                        target_height = int(the_lowest_block.height) - 1
                    block_doc = BlockRepository.create(target_height)
                    app.logger.info(f'Start to crawler a block, height: {target_height}')
                    block = self.w3.eth.get_block(int(block_doc.height))
                    for txn in block.transactions:
                        transaction = self.w3.eth.get_transaction(txn)
                        receipt = self.w3.eth.get_transaction_receipt(txn)
                        from_address = self.upert_address_balance(transaction['from']) if transaction['from'] else None
                        to_address = self.upert_address_balance(transaction['to']) if transaction['to'] else None
                        TransactionRepository.create(dict(
                            hash=self.w3.toHex(txn),
                            block=block_doc,
                            txn_index=transaction.transactionIndex,
                            from_addr=from_address,
                            to_addr=to_address,
                            value=transaction.value,
                            gas=transaction.gas,
                            gas_price=transaction.gasPrice,
                            cumulative_gas_used=receipt.cumulativeGasUsed,
                            effective_gas_price=receipt.effectiveGasPrice,
                            gas_used=receipt.gasUsed
                        ))
                        # TODO, add native eth analyzer

                        for receipt_log in receipt.logs:
                            if analyzer_name := self.detect_analyzer(receipt_log):
                                self.analyzers[analyzer_name].analyze_log(receipt_log)
                            else:
                                self.brute_force_analyze_log(receipt_log)

                    BlockRepository.update(
                        block_doc,
                        dict(
                            base_fee_per_gas=block.baseFeePerGas,
                            gas_limit=block.gasLimit,
                            gas_used=block.gasUsed,
                            analyze_status=True
                        )
                    )
                    BlockRepository.save(block_doc)
                except Exception as err:
                    app.logger.error(f'Error occur in backward crawler, will retry, err: {err}')

            app.logger.info(f'Finish all block !')
