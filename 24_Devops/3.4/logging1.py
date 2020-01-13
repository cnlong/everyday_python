"""
使用Python代码显式的创建loggers，handlers和formatters并分别调用它们的配置函数
"""
import logging
import sys

"""
logging.basicConfig()也属于第一种方式，它只是对loggers，handlers和formatters的配置函数进行了封装。
logging.basicConfig()直接传入输出格式，输出文件名称，输出等级等参数，封装了三个模块，调用更为简单
"""
# 创建一个日志器,logger，并设置级别为DEBUG
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# 创建一个流处理器handler，并设置级别为DEBUG
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# 创建一个格式器，格式化输出，并添加到handler中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 为日志器添加上面创建的处理器handler
logger.addHandler(handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')