# -*- coding: UTF-8 -*-

import mongoengine as me

from common.cld_model import CLDDocument


class ECR20Token(CLDDocument):
    """
    TODO Only consider ERC20 token now
    """
    address = me.StringField(required=True, primary_key=True)
    name = me.StringField()
    symbol = me.StringField()
    decimals = me.IntField()



    meta = {
        'collection': 'erc20_tokens',
        'strict': False,
        'index_background': True,
        'indexes': [],
    }