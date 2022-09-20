# -*- coding: UTF-8 -*-

from .model import Block


class BlockRepository():
    @staticmethod
    def get_larget_unknow_height(curr_height):
        height = curr_height
        if not (block := Block.objects().order_by(Block.height.name).only(Block.height.name).first()):
            height = block.height - 1
        return height
