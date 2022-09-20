# -*- coding: UTF-8 -*-

DEFAULT_APP_NAME = 'CLD'
LOGGER_JOB = 'apscheduler'


DATE_FMT = '%Y-%m-%d'
TIME_FMT = '%H:%M'
DT_FMT = f'{DATE_FMT} {TIME_FMT}:%S'
LOG_DT_FMT = f'{DT_FMT},%03d'
# LOG_FMT_NO_DT = '[%(levelname)7s][%(request_id)s][%(name)s][%(filename)s::%(funcName)s(%(lineno)s)]: %(message)s'
LOG_FMT_NO_DT = '[%(levelname)7s][%(name)s][%(filename)s::%(funcName)s(%(lineno)s)]: %(message)s'
LOG_FMT = '[%(asctime)s]' + LOG_FMT_NO_DT
STR_EMPTY = ''


APS_EVENT_CODE = {
    1: 'EVENT_SCHEDULER_STARTED',
    2: 'EVENT_SCHEDULER_SHUTDOWN',
    4: 'EVENT_SCHEDULER_PAUSED',
    8: 'EVENT_SCHEDULER_RESUMED',
    16: 'EVENT_EXECUTOR_ADDED',
    32: 'EVENT_EXECUTOR_REMOVED',
    64: 'EVENT_JOBSTORE_ADDED',
    128: 'EVENT_JOBSTORE_REMOVED',
    256: 'EVENT_ALL_JOBS_REMOVED',
    512: 'EVENT_JOB_ADDED',
    1024: 'EVENT_JOB_REMOVED',
    2048: 'EVENT_JOB_MODIFIED',
    4096: 'EVENT_JOB_EXECUTED',
    8192: 'EVENT_JOB_ERROR',
    16384: 'EVENT_JOB_MISSED',
    32768: 'EVENT_JOB_SUBMITTED',
    65536: 'EVENT_JOB_MAX_INSTANCES'
}