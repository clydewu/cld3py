# -*- coding: UTF-8 -*-
import mongoengine as me

from common.cld_model import CLDDocument

from .const import AnalyzeStatus


class Block(CLDDocument):
    height = me.DecimalField(force_string=True, primary_key=True)
    base_fee_per_gas = me.DecimalField(force_string=True)
    gas_limit = me.DecimalField(force_string=True)
    gas_used = me.DecimalField(force_string=True)
    analyze_status = me.BooleanField(required=True, default=False)
    # analyze_status = me.EnumField(required=True, default=AnalyzeStatus.ANALYZING)

    meta = {
        'collection': 'blocks',
        'strict': False,
        'index_background': True,
        'indexes': [
        ],
    }