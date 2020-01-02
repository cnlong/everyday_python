import configparser
# 创建configparser实例
config = configparser.ConfigParser()
# 读取配置文件
config.read('config.ini')
# 返回配置文件中所有的节序列（section）也就是每节的标题
print(config.sections())
# 返回某个section中的所有键的序列
print(config.options('ssh'))
# 返回某个section中的某个键的值
print(config.get('ssh', 'host'))
# 添加一个配置文件节点section
config.add_section('ssh2')
print(config.options('ssh2'))
# 添加ssh2节点中键值对
config.set('ssh2', 'host', '192.168.6.165')
config.set('ssh2', 'port', '22')
config.set('ssh2', 'user', 'root')
config.set('ssh2', 'pwd', '123456')
print(config.options('ssh2'))