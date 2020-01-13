"""
Python 3.2中引入的一种新的配置日志记录的方法：用字典来保存logging配置信息。这相对于上面的基于配置文件来保存logging配置信息的方式来说，功能更加强大，也更加灵活，因为我们可以把很多数据转换成字典。
比如：我们可以使用JSON格式的配置文件、YMAL格式的配置文件，然后将它们填充到一个配置字典中；或者，我们也可以用Python代码构建这个配置字典，或者通过socket接收pickled序列化后的配置信息。总之，我们可以使用应用程序可以操作的任何方法来构建这个配置字典。
"""

import logging.config
import yaml

with open("logging.yml", "r") as f_conf:
    dict_conf = yaml.load(f_conf)
    print(dict_conf)
logging.config.dictConfig(dict_conf)

logger = logging.getLogger("simpleExample")

# 日志输出
logger.debug("debug message.")
logger.info("info message.")
logger.warning("warning message.")
logger.error("error message.")
logger.critical("critical message.")