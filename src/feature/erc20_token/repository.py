# -*- coding: UTF-8 -*-

from .model import ECR20Token

class ERC20TokenRepository():
    @staticmethod
    def get_all():
        return ECR20Token.objects()

    @staticmethod
    def get_by_address(address):
        return ECR20Token.objects(address=address).first()

    