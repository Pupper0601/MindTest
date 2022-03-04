"""
-*-coding : UTF-8 -*-
@File     : setToken.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
from configs.logConfig import logger


def setToken(caseData, token):
    def assignment(key):
        if caseData.__dict__[key] is not None:
            if "access_token" in caseData.__dict__[key].keys() and caseData.__dict__[key]["access_token"] is None:
                caseData.__dict__[key]["access_token"] = token
                logger.info(f"{key} 中 token 赋值 成功")
    for i in caseData.__dict__.keys():
        if i == "data":
            assignment(i)
        elif i == "params":
            assignment(i)
        elif i == "headers":
            assignment(i)
