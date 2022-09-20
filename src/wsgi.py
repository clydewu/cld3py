# -*- coding: UTF-8 -*-
# from gevent import monkey
# monkey.patch_all()
from app_factory import AppFactory


app = AppFactory().create_app()
