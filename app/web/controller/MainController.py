# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:09
# @Author  : liuyongliang
# @File    : MainController.py
# @Desc    : MainController.py用于：todo 请添加描述
import os

from flask.templating import render_template

from app.web import controllers
from config import root_dir

RequestMapping = ''


@controllers.route(RequestMapping + '/', methods=['POST', 'GET'])
def mainController():
    indexPathRoot = os.path.join(root_dir, 'webroot/dist')
    indexFilePath = indexPathRoot + '/index'
    return render_template(indexFilePath)
