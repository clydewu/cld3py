# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractclassmethod


class BaseAnalyzer(metaclass=ABCMeta):
    def __init__(self, crawler):
        self.crawler = crawler
        self.w3 = crawler.w3

    @abstractclassmethod
    def analyze_receipt(self):
        pass

    @abstractclassmethod
    def analyze_log(self):
        pass