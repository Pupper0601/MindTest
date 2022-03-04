"""
-*-coding : UTF-8 -*-
@File     : conftest.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""

import pytest
from common.publicApiMethod import PublicApiMethod


@pytest.fixture(scope="session")
def init_session():
    """
    模块级 前置
    :return: 返回 token
    """
    body = PublicApiMethod("/data/api/login/userLoginPhone.yaml")
    access_token = body.apiPost()["access_token"]
    yield access_token
