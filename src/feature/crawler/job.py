# -*- coding: UTF-8 -*-
from .backward import BackwardCrawler 
from .forward import ForwardCrawler


def backward_crawler_job(w3):
    BackwardCrawler(w3).start_crawler()


def forward_crawler_job(w3):
    """ Not be used now """
    ForwardCrawler(w3).start_crawler()
