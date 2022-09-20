# -*- coding: UTF-8 -*-
from .backward import BackwardCrawler 
from .forward import ForwardCrawler


def backward_crawler_job():
    BackwardCrawler().start_crawler()


def forward_crawler_job():
    """ Not be used now """
    ForwardCrawler().start_crawler()
