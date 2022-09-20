# -*- coding: UTF-8 -*-
import mongoengine as me

from common.cld_model import CLDDocument


class Block(CLDDocument):
    height = me.IntField(primary_key=True)

    


    meta = {
        'collection': 'blocks',
        'strict': False,
        'index_background': True,
        'indexes': [
        ],
    }