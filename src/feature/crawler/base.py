# -*- coding: UTF-8 -*-
from flask import current_app as app
from abc import ABCMeta, abstractmethod

from ..address.repository import AddressRepository
from ..tx_analyzer.contract.erc20.analyzer import ERC20Analyzer

class BaseCrawler(metaclass=ABCMeta):
    @abstractmethod
    def start_crawler(self):
        pass

    def __init__(self, w3):
        self.w3 = w3
        self.analyzers = {}
        self.add_analyzer(ERC20Analyzer(self))

    def add_analyzer(self, analyzer):
        # TODO dup-detect?
        self.analyzers[analyzer.name] = analyzer

    def detect_analyzer(self, receipt_log):
        for analyzer in self.analyzers.values():
            if analyzer.is_my_contract(receipt_log.address):
                return analyzer.name
        return None

    def brute_force_analyze_log(self, receipt_log):
        for analyzer in self.analyzers.values():
            try:
                analyzer.analyze_log(receipt_log)
            except Exception as err:
                app.logger.warn(f'Receipt can not be analyzed by this analyzer, address: {receipt_log.address}, analyzer: {analyzer.name}, err: {err}')

    def upert_address_balance(self, addr_str):
        if not (address := AddressRepository.get_by_addr(addr_str)):
            app.logger.info(f'Get a new address, create it, addr: {addr_str}')
            address = AddressRepository.create(dict(
                address=addr_str
            ))
        address.balance=self.w3.eth.get_balance(addr_str)
        AddressRepository.save(address)
        return address