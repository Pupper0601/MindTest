"""
-*-coding : UTF-8 -*-
@File     : baseApi.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
import datetime

import pytest
import requests

from configs.logConfig import logger


class BaseApi:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.timeout = None

    def requestApi(self):
        """
        接口请求
        :return: 返回请求对象
        """
        num = 1
        while num < 4:
            start_time = datetime.datetime.now()
            try:
                logger.info(f"请求参数: "
                            f"{self.url}, "
                            f"{self.method},"
                            f"{self.headers},"
                            f"{self.params},"
                            f"{self.data},"
                            f"{self.json},")
                response = requests.request(
                    method=self.method,
                    url=self.url,
                    headers=self.headers,
                    params=self.params,
                    data=self.data,
                    json=self.json,
                    timeout=self.timeout
                )
                if response.status_code != 200:
                    logger.info(f"接口请求失败: {response.status_code}")
                    pytest.xfail(f"用例失败: 接口请求失败,{response.status_code}")
                else:
                    return response
            except Exception as e:
                logger.error(f"接口请求程序错误: {e}")
            end_time = datetime.datetime.now()
            if int((end_time-start_time).seconds) <= self.timeout:
                logger.info(f"接口 [{self.url}] 请求超时 {(end_time-start_time).seconds}s, 第 {num} 次重试")
                num += 1
        else:
            logger.error(f"[{self.url}] 接口请求错误")
