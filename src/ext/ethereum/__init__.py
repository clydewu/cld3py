# -*- coding: UTF-8 -*-
import os
from web3 import Web3, WebsocketProvider, HTTPProvider


def init_app(app):
    
    # app.w3 = Web3(WebsocketProvider(f'{os.environ["WSS_MAINNET_ENDPOINT_URL"]}'))
    app.w3 = Web3(WebsocketProvider(f'{os.environ["WSS_ROPSTEN_ENDPOINT_URL"]}'))
    # app.w3 = Web3(WebsocketProvider(f'{os.environ["WSS_ENDPOINT_URL"]}'))