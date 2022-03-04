"""
-*-coding : UTF-8 -*-
@File     : test_user_top.PY
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
"""
import pytest
from utils.readYaml import readYaml
from libs.interfaceApi import CaseTest
from libs.setToken import setToken


@pytest.mark.parametrize("case", readYaml("/data/api/user/userTop.yaml")[1:])
class TestLogin:
    def test_login(self, case, init_session):
        case = CaseTest(case)
        case_data = case.setData(init_session)
        res = case.apiPost(case_data)
        case.asserts(res)


if __name__ == '__main__':
    pytest.main("-vs")