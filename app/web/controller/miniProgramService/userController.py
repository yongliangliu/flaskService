# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午12:40
# @Author  : liuyongliang
# @File    : baseUtil.py
# @Desc    : baseUtil.py用于：todo 请添加描述

from app.common.util.httpUtil.responseUtil import writeSuccess2Response
from app.core.model.baseModel.baseModel import Result
from app.web import controllers
from flask import request

RequestMapping = '/miniprogram/user/'


@controllers.route(RequestMapping + 'addUser.json', methods=['GET'])
def addUser():
    result = Result()
    # if request.method != 'GET':
    #     result.setSuccess(False)
    #     resp = writeSuccess2Response(result)
    #     return resp

    result.setData("状态正常")
    result.setSuccess(True)

    return writeSuccess2Response(result)
