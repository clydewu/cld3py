# -*- coding: UTF-8 -*-
from enum import Enum


class AnalyzeStatus(Enum):
    ANALYZING = 'analyzing'
    DONE = 'done'
    FAIL = 'fail'