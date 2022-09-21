# -*- coding: UTF-8 -*-

import mongoengine as me

from common.cld_model import CLDDocument


class Transaction(CLDDocument):
    hash = me.StringField(required=True, primary_key=True)
    block = me.LazyReferenceField('Block')
    txn_index = me.IntField(required=True)
    from_addr = me.LazyReferenceField('Address')
    to_addr = me.LazyReferenceField('Address')
    value = me.DecimalField(force_string=True)

    gas = me.DecimalField(force_string=True)
    gas_price = me.DecimalField(force_string=True)
    
    cumulative_gas_used = me.DecimalField(force_string=True)
    effective_gas_price = me.DecimalField(force_string=True)
    gas_used = me.DecimalField(force_string=True)

    meta = {
        'collection': 'transactions',
        'strict': False,
        'index_background': True,
        'indexes': [
            {'fields': ['block']},
        ],
    }


class ReceiptLog(CLDDocument):
    transaction = me.LazyReferenceField(Transaction, required=True)
    log_index = me.IntField(required=True)
    address = me.ReferenceField('Address')
    block = me.ReferenceField('Block')
    token = me.ReferenceField('ERC20Token', required=True)
    from_addr = me.ReferenceField('Address', required=True)
    to_addr = me.ReferenceField('Address', required=True)
    value = me.DecimalField(force_string=True)



    meta = {
        'collection': 'receipt_logs',
        'strict': False,
        'index_background': True,
        'indexes': [
            {'fields': ['transaction','log_index']},
            {'fields': ['from_addr']},
            {'fields': ['to_addr']},
            {'fields': ['token']},
        ],
    }