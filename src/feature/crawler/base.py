# -*- coding: UTF-8 -*-
from flask import current_app as app
from abc import ABCMeta, abstractmethod

from ..tx_analyzer.contract.erc20.analyzer import ERC20Analyzer

class BaseCrawler(metaclass=ABCMeta):
    @abstractmethod
    def start_crawler(self):
        pass

    def __init__(self):
        self.analyzers = {}
        ERC20Analyzer().register(self)

    def add_analyzer(self, crawler):
        # TODO dup-detect?
        self.analyzers[crawler.name] = crawler

    def detect_analyzer(self, receipt_log):
        analyzer_name = None
        for analyzer in self.analyzers:
            if analyzer.is_my_contract(receipt_log.address):
                analyzer_name = analyzer.name
                break
        return analyzer_name

    def brute_force_analyze_log(self, receipt_log):
        for analyzer in self.analyzers:
            try:
                analyzer.analyze_log(receipt_log)
            except Exception as err:
                app.logger.warn(f'Receipt can not be analyzed by this analyzer, address: {receipt_log.address}, analyzer: {analyzer.name}, err: {err}')