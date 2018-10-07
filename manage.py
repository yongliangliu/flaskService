# -*- coding:utf8 -*-
import os

from app.common.util.baseUtil.baseUtil import multiProcess
from config import Config, root_dir
from app import create_app
from flask_script import Manager

app = create_app('default')
manager = Manager(app, with_default_commands=True)


# 添加默认执行启动服务器的命令
@manager.command
def default_server():
    app.run(debug=True, host=Config.HOST, port=Config.PORT,use_reloader=False)


@manager.command
def run_frond():
    try:
        os.chdir(root_dir + '/webroot/dist')
        os.system(" serve -s ./  -p " + str(Config.FrontPort))
    except:
        pass


def run(name):
    manager.run(default_command=name)


def killport(port):
    commands = "kill `lsof -i:%s | awk '{NR==2 ;print $2}';`" % (port)
    os.system(commands)


if __name__ == '__main__':

    killport(Config.PORT)
    killport(Config.FrontPort)

    data_list = ['run_frond', 'default_server']
    multiProcess(function=run, data_list=data_list, parallel_num=2, type="ProcessPool")
