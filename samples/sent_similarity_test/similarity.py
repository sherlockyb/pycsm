#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : similarity.py

from csm.sent_similarity import EditDistanceSim

if __name__ == '__main__':
    ed_sim = EditDistanceSim()
    sent1 = u'中文句子相似度计算'
    sent2 = u'汉语句子相似度计算'
    tokens1 = [m for m in sent1]
    tokens2 = [m for m in sent2]
    print('score:' + str(ed_sim.get_similarity(tokens1, tokens2)))
