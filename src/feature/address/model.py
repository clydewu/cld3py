# -*- coding: UTF-8 -*-

# -*- coding: UTF-8 -*-
import mongoengine as me

from common.cld_model import CLDDocument


class Address(CLDDocument):
    address = me.StringField(required=True, primary_key=True)
    balance = me.DecimalField(force_string=True)

    meta = {
        'collection': 'address',
        'strict': False,
        'index_background': True,
        'indexes': [
        ],
    }


class AddressToken(CLDDocument):
    address = me.LazyReferenceField('Address', required=True)
    token = me.ReferenceField('ERC20Token', required=True)
    balance = me.DecimalField(force_string=True)

    meta = {
        'collection': 'address_tokens',
        'strict': False,
        'index_background': True,
        'indexes': [
            {'fields': ['address', 'token']},
        ],
    }