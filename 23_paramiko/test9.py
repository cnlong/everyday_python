import configparser

def sevhandler(sec, serverfile):
    """
    服务器文件处理函数
    :param sec: ini文件片段名
    :param severfile: ini文件
    :return: 返回文件中所有服务器信息的字典
    """
    # 服务器信息字典
    sevifo_dict = dict()
    # 服务器列表文件处理
    serverconfig = configparser.ConfigParser()
    serverconfig.read(serverfile)
    # 根据section读取其下面的服务器列表
    servers = serverconfig.options(sec)
    for host in servers:
        sevifo = serverconfig.get(sec, host)
        sevifo_dict[host] = sevifo
    return sevifo_dict

if __name__ == '__main__':
    a = sevhandler('tomcat', 'config2.ini')
    print(a)