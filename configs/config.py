"""
-*-coding : UTF-8 -*-
@File     : config.PY
@Time     : 2022/2/16 14:27
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
@Software : PyCharm
"""

# 项目名称
ObjectName = "MindTest"

# 项目环境
# 正式环境
official = {
    "subject": "https://api.2uchat.cn",
    "tourist": "http://54.223.202.253:8092",
    "member": "http://54.223.202.253:9000"
}
# 测试环境
test = {
    "subject": "http://dev.api.test.2uchat.cn",
    "tourist": "http://52.83.180.187:8092",
    "member": "http://dev.api.test.2uchat.cn"
}
Host = official

# 接口请求等待时间
timeout = 5



