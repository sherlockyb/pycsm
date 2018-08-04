#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : simple_ws.py

"""
Simple Word Segmentation——默认内置的简单分词器
"""

from base import WordSegmentBase


class SimpleWordSegment(WordSegmentBase):

    def __init__(self):
        self.name = 'simple_ws'

    def seg(self, sentence):
        # 按字分词
        tokens = [m for m in sentence]
        return tokens, ['n']*len(tokens)
