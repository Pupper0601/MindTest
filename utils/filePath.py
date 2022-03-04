"""
-*-coding : UTF-8 -*-
@File     : RootPath.PY
@Time     : 2022/2/15 17:50
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
@Software : PyCharm
"""
import os
from configs.config import ObjectName


def absoluteFilePath(file_path):
    """
    文件绝对路径
    :param file_path: 文件相对路径
    :return:
    """
    object_path = os.path.abspath(os.path.dirname(__file__)).split(f'{ObjectName}')[0] + f'{ObjectName}'
    return object_path + file_path


if __name__ == '__main__':
    a = absoluteFilePath("/data/api/login/login-login-phone.yaml")
    print(a)