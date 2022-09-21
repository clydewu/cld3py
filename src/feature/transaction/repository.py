# -*- coding: UTF-8 -*-

from .model import Transaction, ReceiptLog

class TransactionRepository():
    @staticmethod
    def create(attrs, *args, **kwargs):
        transaction = Transaction(**attrs)
        return TransactionRepository.save(transaction, *args, **kwargs)

    @staticmethod
    def save(transaction, *args, **kwargs):
        return transaction.save(*args, **kwargs)


class ReceiptLogRepository():
    @staticmethod
    def create(attrs, *args, **kwargs):
        receipt_log = ReceiptLog(**attrs)
        return ReceiptLogRepository.save(receipt_log, *args, **kwargs)

    @staticmethod
    def save(receipt_log, *args, **kwargs):
        return receipt_log.save(*args, **kwargs)