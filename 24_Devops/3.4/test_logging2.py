import logging


# 将日志输出到指定文件中，并且输出级别为info
logging.basicConfig(filename='app.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')