# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:07
# @Author  : liuyongliang
# @File    : BaseWebPythonController.py
# @Desc    : BaseWebPythonController.py用于：todo 请添加描述



from flask import request

from app.common.util.httpUtil.responseUtil import writeSuccess2Response
from app.core.model.baseModel import Result
from app.core.service.webPythonService import BaseWebPythonService
from app.web import controllers

RequestMapping = '/api/WebPythonService'


@controllers.route(RequestMapping + '/runScript.json', methods=['POST'])
def runScript():
    result = Result()

    if request.method != 'POST':
        result.setSuccess(False)
        resp = writeSuccess2Response(result)
        return resp

    requestBody = request.get_data()

    ret_code, ret_data = BaseWebPythonService.run(requestBody)
    result = Result()

    result.setData(ret_data)
    result.setSuccess(ret_code)
    return writeSuccess2Response(result)
