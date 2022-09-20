# -*- coding: UTF-8 -*-
import logging
import logging.handlers

from flask import Flask
from flask.logging import default_handler
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_restx import Api
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
# from flask_log_request_id import RequestID, RequestIDLogFilter
# from apscheduler.schedulers.gevent import GeventScheduler
# from apscheduler.jobstores.mongodb import MongoDBJobStore
import urllib3

from const import DEFAULT_APP_NAME, APS_EVENT_CODE, LOG_FMT

scheduler = APScheduler(scheduler=BackgroundScheduler())

class AppFactory():

    def create_app(self, name=DEFAULT_APP_NAME):
        app = Flask(name or __name__)
        CORS(app)
        self.__setup_main_logger(app, logging.DEBUG)
        app.db = MongoEngine(app, app.config)

        app.csw_api = csw_api = Api(app, title=DEFAULT_APP_NAME)
        # self.__create_bundled_loggers(app, csw_api)
        self.__init_apscheduler(app)
        self.__init_modules(app, csw_api)
        # self.__create_endpoint_loggers(app, csw_api)
        # self.__error_handling(app, csw_api)
        app.logger.info('Application initial success.')  # pylint: disable=no-member
        urllib3.disable_warnings()
        return app

    def __setup_main_logger(self, app, level=logging.INFO):
        logger = app.logger
        logger.removeHandler(default_handler)
        self.__setup_logger(app, logger.name, level)

    def __setup_logger(self, app, logger_name, level=logging.INFO):
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(fmt=LOG_FMT))
        # stream_handler.addFilter(RequestIDLogFilter())
        logger.addHandler(stream_handler)

        return logger

    def __init_apscheduler(self, app):
        app.scheduler = scheduler
        app.scheduler.init_app(app)

        from apscheduler.events import EVENT_JOB_ADDED, EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, EVENT_JOB_MISSED, EVENT_JOB_REMOVED, EVENT_JOB_SUBMITTED

        def job_event(event):
            app.logger.info(f'Job event occur, job: {event.job_id}, event: {APS_EVENT_CODE.get(event.code)}')

        app.scheduler.add_listener(
            job_event,
            EVENT_JOB_ADDED | EVENT_JOB_ERROR | EVENT_JOB_EXECUTED | EVENT_JOB_MISSED | EVENT_JOB_REMOVED | EVENT_JOB_SUBMITTED
        )

        app.scheduler.start()


    def __init_modules(self, app, api):
        from ext.ethereum import init_app as init_ethereum
        from feature.crawler import init_app as init_crawler

        init_ethereum(app)
        init_crawler(app)