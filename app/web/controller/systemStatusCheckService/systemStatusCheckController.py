# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:08
# @Author  : liuyongliang
# @File    : systemStatusCheckController.py
# @Desc    : systemStatusCheckController.py用于：todo 请添加描述


from app.common.util.httpUtil.responseUtil import writeSuccess2Response

from app.core.model.baseModel import Result
from app.web import controllers
from flask import request

RequestMapping = ''


@controllers.route(RequestMapping + '/checkService', methods=['GET'])
def systemStatusCheckController():
    result = Result()
    if request.method != 'GET':
        result.setSuccess(False)
        resp = writeSuccess2Response(result)
        return resp

    result.setData("状态正常")
    result.setSuccess(True)

    return writeSuccess2Response(result)
