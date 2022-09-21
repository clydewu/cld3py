# -*- coding: UTF-8 -*-

from .model import Block


class BlockRepository():
    @staticmethod
    def create(height, *args, **kwargs):
        block = Block(height=height)
        return BlockRepository.save(block, force_insert=True, *args, **kwargs)

    @staticmethod
    def update(block, attrs, *args, **kwargs):
        block.update_attr(attrs)
        return BlockRepository.save(block, *args, **kwargs)

    @staticmethod
    def save(block, *args, **kwargs):
        return block.save(*args, **kwargs)

    @staticmethod
    def get_the_lowest_block():
        return Block.objects().order_by(Block.height.name).only(Block.height.name).first()
 