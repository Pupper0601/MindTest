"""
-*-coding : UTF-8 -*-
@File     : LogConfig.PY
@Time     : 2022/2/17 11:02
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
@Software : PyCharm
"""
import os.path
import time
from loguru import logger
from utils.filePath import absoluteFilePath


# 如果文件夹不存在,则创建文件夹
filePath = absoluteFilePath("/outFiles/logs")
if not os.path.isdir(filePath):
    os.mkdir(filePath)

print(filePath)

# 日志文件时间
log_name = time.strftime("%Y_%m_%d %H_%M_%S")

logger.add(
    f"{filePath}/{time.strftime('%Y_%m_%d %H_%M_%S')}.log",      # 日志输出到指定文件
    encoding="utf-8",   # 日志输出编码
    enqueue=True,       # 开启异步写入
    retention="5 days",  # 设置保留时长
    rotation="1 MB",     # 限定日志大小
    compression="zip",  # 指定压缩格式
)
