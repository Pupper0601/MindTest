"""
-*-coding : UTF-8 -*-
@File     : baseAssert.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
import json

import allure
import pytest

from configs.logConfig import logger


class BaseAssert:
    def __init__(self, assertData, response):
        """
        遍历字典,获取key, value 自动生成类属性
        :param assertData: 字典
        """
        self.res = response
        for key, value in assertData.items():
            setattr(self, key, value)

    def state(self):
        """
        状态码断言
        :return:
        """
        code = self.res.status_code
        if hasattr(self, "statusCode"):
            logger.info(f"状态码断言: {code} == {self.__dict__['statusCode']}")
            allure.attach(f"{code} == {self.__dict__['statusCode']}", "参数", allure.attachment_type.JSON)
            assert code == self.__dict__["statusCode"],{f"{code} == {self.__dict__['statusCode']}"}
        else:
            logger.info(f"该属性不存在: statusCode")

    def assertBody(self, key):
        """
        响应体 断言
        :param key: 断言的字段(字段名需要与响应体一致)
        :return:
        """
        body = json.loads(self.res.text)
        logger.info(body)
        if hasattr(self, key):
            if key in body.keys():
                logger.info(f"{body[key]} == {self.__dict__[key]}")
                allure.attach(f"{body[key]} == {self.__dict__[key]}", "参数", allure.attachment_type.JSON)
                assert body[key] == self.__dict__[key], {f"{body[key]} == {self.__dict__[key]}"}
            else:
                logger.info(f"断言设置错误: {key} 不在 {body} 中")
                pytest.xfail("用例失败: 断言设置错误")
        else:
            logger.info(f"该属性不存在: {key}")
