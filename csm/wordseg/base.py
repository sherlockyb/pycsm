#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : base.py

"""
Base Word Segmentation——分词器基类
"""


class WordSegmentBase:

    def __init__(self):
        self.name = 'none'

    def seg(self, sentence):
        return [sentence], ['n']
