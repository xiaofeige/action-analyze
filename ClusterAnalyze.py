#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: ClusterAnalyze.py
@time: 2017/3/16 14:23
"""

import json


def init_api_dist():
    """
    从data目录中获取到api列表，初始化一个字典返回
    :return:描述API列表的一个字典
    """
    pass
    return {}


def load_file(filename):
    """
    加载行为文件转换为词向量
    思路：根据对应api编号，统计每个api调用次数将其转为描述xxxapi调用次数的一维向量。
    :param filename:文件路径
    :return:api调用矩阵
    """
    file_in = open(filename, 'r')

    api_dist = init_api_dist()
    while True:
        line = file_in.readline()
        api = line[2]
        api_dist[api] += 1

    file_in.close()
    # 将字典转换成vector返回
    api_vec = []
    for (k, v) in api_dist.items():
        api_vec.append(v)
    return api_vec


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

