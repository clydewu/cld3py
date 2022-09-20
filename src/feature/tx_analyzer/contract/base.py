# -*- coding: UTF-8 -*-
from abc import abstractmethod
from ....const import STR_EMPTY
from ..base import BaseAnalyzer


class BaseERCAnalyzer(BaseAnalyzer):
    name = STR_EMPTY
    abi = None

    def register(self, crawler):
        crawler.add_analyzer(crawler)

    @abstractmethod
    def is_my_contract(self, address):
        pass

    def analyze_receipt(self):
        raise NotImplementedError('This ERC analyzer only support analyze by each receipt log now')
