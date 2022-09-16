# -*- coding: UTF-8 -*-
# from gevent import monkey
# monkey.patch_all()
from app_factory import AppFactory

app = AppFactory().create_app()

# if __name__ == '__main__':
#     app.sio.run(app, host='0.0.0.0', port=app.config.get('RUN_PORT'), debug=app.config.get('DEBUG'))
