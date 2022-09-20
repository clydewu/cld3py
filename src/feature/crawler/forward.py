# -*- coding: UTF-8 -*-

from .base import BaseCrawler

class ForwardCrawler(BaseCrawler):
    def start_crawler(self):
        raise NotImplementedError()