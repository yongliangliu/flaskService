# coding=utf-8
import json, os

from flask import Response

from app.common.util.baseUtil.baseUtil import object2json


def writeSuccess2Response(result):
    data = object2json(result)
    resp = Response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp
