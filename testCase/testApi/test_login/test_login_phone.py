"""
-*-coding : UTF-8 -*-
@File     : test_login.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""

import pytest
from utils.readYaml import readYaml
from libs.interfaceApi import CaseTest


@pytest.mark.parametrize("case", readYaml("/data/api/login/userLoginPhone.yaml")[1:])
class TestLogin:
    def test_login(self, case):
        case = CaseTest(case)
        case_data = case.setData()
        res = case.apiPost(case_data)
        case.asserts(res)
