# -*- coding: UTF-8 -*-

from .model import ERC20Token

class ERC20TokenRepository():
    @staticmethod
    def get_all():
        return ERC20Token.objects()

    @staticmethod
    def get_by_address(address):
        return ERC20Token.objects(address=address).first()

    @staticmethod
    def new(address=None, name=None, symbol=None, decimals=None):
        return ERC20Token(address=address, name=name, symbol=symbol, decimals=decimals)

    @staticmethod
    def save(token):
        return token.save()
