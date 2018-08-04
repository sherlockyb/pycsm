#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : csm.py

"""
Chinese Sentence Match——中文句子匹配
"""

from wordseg.simple_ws import SimpleWordSegment
from sent_similarity import EditDistanceSim


class SentenceMatch:

    def __init__(self,
                 sent_similarity=None,      # 句子相似度计算器
                 word_segment=None,         # 分词器
                 match_min_score=0.5):      # 最小匹配得分
        if sent_similarity is None:
            self.sent_similarity = EditDistanceSim()
        if word_segment is None:
            self.ws = SimpleWordSegment()
        self.match_min_score = match_min_score

    def match(self, sent1, sent2, need_seg=True):
        if sent1 == sent2:
            return True, 1.0
        if need_seg:
            tokens1 = self.ws.seg(sent1)[0]
            tokens2 = self.ws.seg(sent2)[0]
        else:
            tokens1 = [m for m in sent1]
            tokens2 = [m for m in sent2]

        score = self.sent_similarity.get_similarity(tokens1, tokens2)

        return True if score > self.match_min_score else False, score
