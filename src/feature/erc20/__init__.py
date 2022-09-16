# -*- coding: UTF-8 -*-
import os
from datetime import datetime

import arrow
from web3 import Web3, WebsocketProvider, HTTPProvider

from .job import main_job


def init_app(app, api):
    # app.w3 = Web3(WebsocketProvider(f'{os.environ["WSS_ENDPOINT_URL"]}'))
    app.w3 = Web3(HTTPProvider(f'{os.environ["HTTPS_ENDPOINT_URL"]}'))
    app.w3.eth.get_block('latest')

    app.scheduler.add_job(
        main_job.__name__,
        main_job,
        # trigger=CronTrigger.from_crontab(app.config[config_key]),
        next_run_time=arrow.utcnow().shift(seconds=0).datetime,
        max_instances=1,
        replace_existing=True,
        misfire_grace_time=None
    )