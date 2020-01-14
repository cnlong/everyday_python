import logging


# 配置日志的输出格式
# 时间逗号后面是毫秒时间
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')