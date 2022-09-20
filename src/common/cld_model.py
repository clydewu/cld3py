# -*- coding: UTF-8 -*-
from datetime import datetime
import mongoengine as me
from mongoengine import Document, QuerySet


class CLDQuerySet(QuerySet):
    pass


class CLDDocument(Document):
    create_time = me.DateTimeField(required=True, default=datetime.utcnow)
    update_time = me.DateTimeField(required=True, default=datetime.utcnow)
    meta = {
        'abstract': True,
        'queryset_class': CLDQuerySet
    }