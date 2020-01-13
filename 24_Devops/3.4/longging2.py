import logging.config


# 读取日志配置文件内容
"""
fileConfig()函数
该函数实际上是对configparser模块的封装,读取的ini配置文件格式
"""
"""
日志配置文件解析：父级日志器root,子级日志器simpleExample
propagate=0
simpleExample这个logger在处理完日志记录后，把日志记录传递给了上级的root logger再次做处理，所以才会有两个地方都有日志记录的输出。通常，我们都需要显式的指定propagate的值为0，防止日志记录向上层logger传递
"""
logging.config.fileConfig('logging2.cnf')
# 创建一个日志器
"""
当一个日志器没有被设置任何处理器时，系统会去查找该日志器的上层日志器所设置的日志处理器来处理日志记录。simpleExample1在配置文件中没有被定义，因此logging.getLogger(simpleExample1)这行代码是获取了一个logger实例，并没有给它设置任何处理器，但是它的上级日志器----root logger在配置文件中有定义且设置了一个FileHandler处理器，simpleExample1处理器最终通过这个FileHandler处理器将日志记录输出到logging.log文件中了。
"""
logger= logging.getLogger('a')

# 会寻找配置文件中同名的logger日志器，找不到，会查找上级日志器来处理他
# logger= logging.getLogger('root')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')