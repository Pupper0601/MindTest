"""
-*-coding : UTF-8 -*-
@File     : dataSort.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""

from common.baseApi import BaseApi
from configs.logConfig import logger
from utils.md5 import getMd5
from configs.config import Host, timeout


class DataIntegrate(BaseApi):

    def __init__(self, dataAll):
        super().__init__()
        self.data_all = dataAll

    def setData(self):
        try:
            for key, value in self.data_all.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            self.setUrl()
            self.passwordEncrypt()
        except Exception as e:
            logger.error(f"接口数据设置错误: {e}")

    def setUrl(self):
        try:
            self.url = Host[self.data_all["host"]] + self.url
            self.timeout = timeout
        except Exception as e:
            logger.error(f" url 拼接错误: {e}")

    def passwordEncrypt(self):
        try:
            if self.data is not None:
                if "password" in self.data.keys():
                    self.data["password"] = getMd5(self.data["password"])
                    logger.info(f"password 加密: {self.data['password']}")
        except Exception as e:
            logger.error(f"密码 md5 加密错误: {e}")
