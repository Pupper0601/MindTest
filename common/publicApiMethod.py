"""
-*-coding : UTF-8 -*-
@File     : getToken.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
import ast
import json

import allure

from libs.dataSort import DataIntegrate
from configs.logConfig import logger
from utils.readYaml import readYaml


class PublicApiMethod:
    def __init__(self, file_path):
        self.data = readYaml(file_path)[1]

    def apiPost(self):
        try:
            obj_data = DataIntegrate(self.data)
            obj_data.setData()
            res_body = json.loads(obj_data.requestApi().text)["data"]
            logger.info(f"{res_body}")
            allure.attach(f"{res_body}", "登录接口响应", allure.attachment_type.JSON)
            return res_body
        except Exception as e:
            logger.error(f"登录接口错误: {e}")


if __name__ == '__main__':
    a = PublicApiMethod()
    a.apiPost()