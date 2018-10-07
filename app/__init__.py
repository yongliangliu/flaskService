# -*- coding:utf8 -*-
__all__ = ['biz', 'common', 'core', 'conf']

import os
from flask import Flask
from config import root_dir

route_list = []


def fetchRoute(blueprint, prefix=None):
    tmpList = [blueprint, prefix]
    route_list.append(tmpList)


def create_app(config_name):
    app = Flask(__name__)

    app_dir = os.path.join(root_dir, 'app')
    # 逐个执行各个路由映射脚本，添加到route_list中
    # for routes in os.listdir(app_dir):
    #     rou_path = os.path.join(app_dir, routes)
    #     if (not os.path.isfile(rou_path)) and routes != 'static' and routes != 'templates':
    __import__('app.' + 'web')
    for blueprints in route_list:
        if blueprints[1] != None:
            app.register_blueprint(blueprints[0], url_prefix=blueprints[1])
        else:
            app.register_blueprint(blueprints[0])
    return app
