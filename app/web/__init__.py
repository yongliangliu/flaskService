# -*- coding:utf8 -*-

__all__ = ['biz', 'common', 'core', 'conf']
import os
from flask import Blueprint
from config import root_dir

controller_root = os.path.join(root_dir, 'app/web/controller')

import app

controllers = Blueprint('controller', __name__)
app.fetchRoute(controllers, '')

# 动态引入web.controller下面所有带Controller的文件的路由
for root, dirs, files in os.walk(controller_root):
    for f in files:
        if "__init__.py" not in f and '.pyc' not in f and '.py' in f and 'Controller' in f:
            controller_name = 'app.web.controller' + os.path.join(root, f).replace(controller_root, '').replace('/',
                                                                                                                '.')[
                                                     :-3]
            __import__(controller_name)
