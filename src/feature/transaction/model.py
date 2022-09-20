# -*- coding: UTF-8 -*-

import mongoengine as me

from common.cld_model import CLDDocument


class Transaction(CLDDocument):
    hash = me.StringField(required=True, primary_key=True)
    block = me.ReferenceField('block')
    token = me.ReferenceField('token', required=True)
    from_addr = me.ReferenceField('address', required=True)
    to_addr = me.ReferenceField('address', required=True)
    value = me.IntField()



    meta = {
        'collection': 'transactions',
        'strict': False,
        'index_background': True,
        'indexes': [
            {'fields': ['from_addr']},
            {'fields': ['to_addr']},
            {'fields': ['token']},
        ],
    }