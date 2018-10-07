# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:04
# @Author  : liuyongliang
# @File    : baseUtil.py
# @Desc    : baseUtil.py用于：todo 请添加描述



import json
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool


def object2json(object):
    return json.dumps(object, default=lambda obj: obj.__dict__, sort_keys=True, ensure_ascii=False)


def object2dict(object):
    jsonData = object2json(object)
    return json.loads(jsonData)


def multiProcess(function, data_list, parallel_num, type, return_swith=False):
    if parallel_num > 20:
        parallel_num = 20
    if type == "multithread":
        pool = ThreadPool(parallel_num)
    else:
        pool = Pool(parallel_num)
    if return_swith == True:
        result = pool.map(function, data_list)
        pool.close()
        pool.join()
        return result
    else:
        pool.map(function, data_list)
        pool.close()
        pool.join()
