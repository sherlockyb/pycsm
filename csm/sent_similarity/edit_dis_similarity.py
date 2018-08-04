#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/4
# @Author  : sherlockyb
# @File    : edit_dis_similarity.py


class EditDistanceSim:

    def __init__(self):
        pass

    @classmethod
    def get_similarity(cls, tokens1, tokens2):
        matrix = [[i+j for j in range(len(tokens2)+1)] for i in range(len(tokens1)+1)]

        for i in range(1, len(tokens1)+1):
            for j in range(1, len(tokens2)+1):
                if tokens1[i-1] == tokens2[j-1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)
        dis = matrix[len(tokens1)][len(tokens2)]*1.0
        max_len = max(len(tokens1), len(tokens2))

        return 1.0 - dis/max_len
