"""
-*-coding : UTF-8 -*-
@File     : Md5.PY
@Time     : 2022/2/17 11:32
@Author   : Pupper
@Email    : pupper.cheng@gmail.com
@Software : PyCharm
"""
import hashlib
from configs.logConfig import logger


def getMd5(value, long=True, lower=True):
    """
    md5 加密
    :param value: 待加密的值
    :param long: 32 位或 16 位,默认为 32 位
    :param lower: 大写或小写,默认为小写
    :return: 加密后的值
    """
    try:
        md5 = hashlib.md5()
        md5.update(value.encode('utf-8'))
        if long:
            if lower:
                return (md5.hexdigest()).lower()
            else:
                return (md5.hexdigest()).upper()
        else:
            if lower:
                return (md5.hexdigest())[8:-8].lower()
            else:
                return (md5.hexdigest())[8:-8].upper()
    except Exception as e:
        logger.error(f'md5 加密程序错误:{e}')
        return None


if __name__ == '__main__':
    print(getMd5("000000"))