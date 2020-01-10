import configparser
import getpass


def sevhandler(sec, serverfile):
    """
    返回服务器列表
    :param sec: 片段名
    :param serverfile: 文件名
    :return: 服务器列表
    """
    sevinfo_dict = dict()
    serverconfig = configparser.RawConfigParser()
    serverconfig.read(serverfile)
    servers = serverconfig.options(sec)
    for host in servers:
        sevinfo = serverconfig.get(sec, host)
        sevinfo_dict[host] = sevinfo
    return sevinfo_dict

# a = sevhandler('prd', 'config3.ini')
# for key, value in a.items():
#     host = value.split(',')[0]
#     print(type(host))
#     oldpwd = value.split(',')[1]
#     print(oldpwd)

pwd = getpass.getpass("your password")
