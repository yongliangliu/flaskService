# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午12:40
# @Author  : liuyongliang
# @File    : baseUtil.py
# @Desc    : baseUtil.py用于：todo 请添加描述

import os
import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os

import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

backlog = 512
debug = True
loglevel = 'debug'
bind = '0.0.0.0:443'
bind ='127.0.0.1:8888'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'


chdir = '/home/lyl/pythonService'

daemon = True

reload = True

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
#worker_class = 'gunicorn.workers.ggevent.GeventWorker'
worker_class='geventwebsocket.gunicorn.workers.GeventWebSocketWorker'
#worker_class = 'flask_sockets.worker'
threads = 4

x_forwarded_for_header = 'X-FORWARDED-FOR'