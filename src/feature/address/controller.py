# -*- coding: UTF-8 -*-
from flask_restx import Namespace

from flask_restx import Resource


api_ns = Namespace("Address", description="Address")


@api_ns.route("", endpoint='Address')
class AddressResource(Resource):
    def get(self):
        return True
