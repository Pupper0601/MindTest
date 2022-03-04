import yaml
import os
from configs.logConfig import logger
from utils.filePath import absoluteFilePath


def readYaml(file_dir):
    """
    读取 yaml 信息
    :param file_dir: yaml 文件路径
    :return:
    """
    try:
        file_dir = absoluteFilePath(file_dir)
        if os.path.exists(file_dir):
            with open(file_dir, "r", encoding="UTF-8") as file:
                data = yaml.safe_load(file.read())
                logger.info(data)
                return data
        else:
            logger.info(f"用例文件不存在:{file_dir}")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    readYaml("/data/api/login/userLoginPhone.yaml")
