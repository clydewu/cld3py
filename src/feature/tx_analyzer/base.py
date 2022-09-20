# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractclassmethod


class BaseAnalyzer(metaclass=ABCMeta):
    @abstractclassmethod
    def analyze_receipt(self):
        pass

    @abstractclassmethod
    def analyze_log(self):
        pass