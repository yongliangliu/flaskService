# -*- coding:utf8 -*-
import sys
import os

root_dir = os.path.abspath(os.path.dirname(__file__))

reload(sys)
sys.setdefaultencoding('utf-8')


class Config:
    # 设置端口
    HOST = "0.0.0.0"
    PORT = 5000
    FrontPort = 7001
