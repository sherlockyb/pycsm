#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : csm.py

from csm import SentenceMatch

if __name__ == '__main__':
    sm = SentenceMatch()
    sent1 = u'中文句子相似度计算'
    sent2 = u'汉语句子相似度计算'
    print('match result:' + str(sm.match(sent1, sent2)))
