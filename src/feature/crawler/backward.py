# -*- coding: UTF-8 -*-

from flask import current_app as app
from app_factory import scheduler

from ..block.repository import BlockRepository
from .base import BaseCrawler


class BackwardCrawler(BaseCrawler):
    def start_crawler(self):
        with scheduler.app.app_context():
            w3 = app.w3
            latest_block_number = target_height = w3.eth.block_number
            while target_height < 0:
                try:
                    target_height = BlockRepository.get_larget_unknow_height(latest_block_number.height)
                    app.logger.error(f'Start to crawler block, height: {target_height}')
                    target_block = w3.eth.get_block(target_height)
                    for tx in target_block.transactions:
                        receipt = w3.eth.get_transaction_receipt(tx)
                        # TODO, add native eth analyzer

                        for receipt_log in receipt.logs:
                            if analyzer_name := self.detect_analyzer(receipt_log):
                                self.analyzers[analyzer_name].analyze_log(receipt_log)
                            else:
                                self.brute_force_analyze_log(receipt_log)
                except Exception as err:
                    app.logger.error(f'Error occur in backward crawler, will retry, err: {err}')

            app.logger.info(f'Finish all block !')