import os
import shutil
import pytest


def del_file():
    """
    暴力删除 日志文件 和 报告文件,重新创建文件夹
    :return:
    """
    shutil.rmtree("./outFiles/logs")
    os.mkdir("./outFiles/logs")
    shutil.rmtree("./outFiles/reports/data")
    os.mkdir("./outFiles/reports/data")
    shutil.rmtree("./outFiles/reports/tmp")
    os.mkdir("./outFiles/reports/tmp")


if __name__ == '__main__':
    del_file()
    pytest.main(["-vs", "./testCase/testApi", "-n=auto", '--alluredir', './outFiles/reports/data'])
    os.system("allure generate ./outFiles/reports/data -o ./outFiles/reports/tmp")
    # os.system("allure serve ./outFiles/reports/tmp")
