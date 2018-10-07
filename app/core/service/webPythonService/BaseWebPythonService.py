# -*- coding: utf-8 -*-
# @Time    : 18/8/21 下午11:08
# @Author  : liuyongliang
# @File    : BaseWebPythonService.py
# @Desc    : BaseWebPythonService.py用于：todo 请添加描述


import os, sys, subprocess, tempfile, time

TempFile = tempfile.mkdtemp(suffix='_', prefix='python_')
# 文件名
FileNum = int(time.time() * 1000)
# python编译器位置
EXEC = sys.executable


# 获取python版本
def get_version():
    v = sys.version_info
    version = "python %s.%s" % (v.major, v.minor)
    return version


# 获得py文件名
def get_pyname():
    global FileNum
    return '%d' % FileNum


# 接收代码写入文件
def write_file(pyname, code):
    fpath = os.path.join(TempFile, '%s.py' % pyname)
    with open(fpath, 'w') as f:
        f.write(code)
    print('file path: %s' % fpath)
    return fpath


# 编码
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

        # 主执行函数


def run(code):
    code = checkScript(code=code)

    r = dict()
    r["version"] = get_version()
    pyname = get_pyname()

    fpath = write_file(pyname, code)
    try:
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        outdata = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["code"] = 'Error'
        r["output"] = decode(e.output)
        return False, r
    else:
        # 成功返回的数据
        r['output'] = outdata
        r["code"] = "Success"
        return True, r
    finally:
        # 删除文件(其实不用删除临时文件会自动删除)
        try:
            os.remove(fpath)
        except Exception as e:
            exit(1)


def checkScript(code):
    code = "# -*- coding: utf-8 -*-\n" + code
    return code


if __name__ == '__main__':
    code = "print(11);print(22)"
    print(run(code))
