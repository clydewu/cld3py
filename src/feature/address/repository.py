# -*- coding: UTF-8 -*-

from .model import Address, AddressToken



class AddressRepository():

    @staticmethod
    def get_by_addr(addr):
        return Address.objects(address=addr).first()

    @staticmethod
    def create(attrs, *args, **kwargs):
        address = Address(**attrs)
        return AddressRepository.save(address, *args, **kwargs)

    @staticmethod
    def save(address, *args, **kwargs):
        return address.save(*args, **kwargs)


class AddressTokenRepository():

    @staticmethod
    def get(addr, token):
        return AddressToken.objects(address=addr, token=token).first()

    @staticmethod
    def create(attrs, *args, **kwargs):
        address = AddressToken(**attrs)
        return AddressTokenRepository.save(address, force_insert=True, *args, **kwargs)

    @staticmethod
    def save(address, *args, **kwargs):
        return address.save(*args, **kwargs)