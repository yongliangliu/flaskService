# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:07
# @Author  : liuyongliang
# @File    : ImageServiceController.py
# @Desc    : ImageServiceController.py用于：todo 请添加描述
import json

from flask import request

from app.common.util.httpUtil.responseUtil import writeSuccess2Response
from app.core.model.baseModel import Result
from app.core.util.imageUtil import ImageDiff
from app.web import controllers

RequestMapping = '/api'


@controllers.route(RequestMapping + '/imageDiff.json', methods=['POST', 'GET'])
def imageDiff():
    result = Result()

    if request.method != 'POST':
        result.setSuccess(False)
        resp = writeSuccess2Response(result)
        return resp

    request_body = json.loads(request.get_data())
    baseImage = request_body['baseImage']
    compareImage = request_body['compareImage']

    ret_code, ret_data = ImageDiff.ImageDiff(baseImage, compareImage)
    result = Result()

    result.setData(ret_data)
    result.setSuccess(ret_code)

    return writeSuccess2Response(result)
