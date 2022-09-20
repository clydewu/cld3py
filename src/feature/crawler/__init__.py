# -*- coding: UTF-8 -*-
import arrow

from .job import backward_crawler_job, forward_crawler_job


def init_app(app):
    app.scheduler.add_job(
        backward_crawler_job.__name__,
        backward_crawler_job,
        # trigger=CronTrigger.from_crontab(app.config[config_key]),
        next_run_time=arrow.utcnow().shift(seconds=0).datetime,
        max_instances=1,
        replace_existing=True,
        misfire_grace_time=None
    )


    app.scheduler.add_job(
        forward_crawler_job.__name__,
        forward_crawler_job,
        # trigger=CronTrigger.from_crontab(app.config[config_key]),
        next_run_time=arrow.utcnow().shift(seconds=0).datetime,
        max_instances=1,
        replace_existing=True,
        misfire_grace_time=None
    )