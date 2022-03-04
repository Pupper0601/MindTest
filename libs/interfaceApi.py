"""
-*-coding : UTF-8 -*-
@File     : interfaceApi.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
import json
import allure
import pytest

from common.baseAssert import BaseAssert
from libs.dataSort import DataIntegrate
from configs.logConfig import logger
from libs.setToken import setToken


class CaseTest:
    def __init__(self, data):
        allure.dynamic.feature(data["featureName"])
        allure.dynamic.story(data["storyName"])
        allure.dynamic.title(data["caseTitle"])
        self.data = data

    @allure.step("整合测试数据")
    def setData(self, token=None):
        obj_data = DataIntegrate(self.data)
        obj_data.setData()
        setToken(obj_data, token)
        allure.attach(f"{obj_data.__dict__}", "参数", allure.attachment_type.JSON)
        return obj_data

    @allure.step("接口请求")
    def apiPost(self, obj_data):
        logger.info(obj_data.__dict__.items())
        response = obj_data.requestApi()
        allure.attach(f"{response.request.url}, {response.request.method}", "请求方法", allure.attachment_type.JSON)
        allure.attach(f"{response.request.headers}", "请求头", allure.attachment_type.JSON)
        allure.attach(f"{response.request.body}", "请求体", allure.attachment_type.JSON)
        allure.attach(f"{response.headers}", "响应头", allure.attachment_type.JSON)
        allure.attach(f"{response.text}", "响应体", allure.attachment_type.JSON)
        return response

    @allure.step("断言")
    def asserts(self, response):
        obj = BaseAssert(self.data["asserts"], response)
        obj.state()
        for key in self.data["asserts"].keys():
            if key != "statusCode":
                obj.assertBody(key)
