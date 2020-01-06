"""
多线程，多台服务批量执行命令
"""
import configparser
import paramiko
# import time
import threading


def sevhandler(sec, serverfile):
    """
    服务器文件处理函数
    :param sec: ini文件片段名
    :param serverfile: ini文件
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


# class SShClient(object):
#     def __init__(self, host, port=22, username='sit_yunwei', passwd='CKH@123$%^YunWei_sit'):
#         self.host = host
#         self.port = port
#         self.username = username
#         self.pwd = passwd
#         self.sshclient = paramiko.SSHClient()
#         self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.sshclient.connect(hostname=self.host,
#                                port=self.port,
#                                username=self.username,
#                                password=self.pwd)
#
#     def run_cmd(self, cmd):
#         stdin, stdout, stderr = self.sshclient.exec_command(cmd)
#         result = stdout.read()
#         if len(result) == 0:
#             print("Error: %s" % (stderr.read().decode('utf-8')))
#         else:
#             print(result.decode('utf-8'), end='')
#
#     def client_close(self):
#         self.sshclient.close()
def cmdhandler(cmdfile):
    cmd_list = list()
    with open(cmdfile) as f:
        while True:
            cmd = f.readline()
            if not cmd:
                break
            cmd_list.append(cmd.strip('\n'))
    return cmd_list


def ssh(cmdfile, host, port=22, username='sit_yunwei', passwd='CKH@123$%^YunWei_sit'):
    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(hostname=host, port=port, username=username, password=passwd)
        cmd_list = cmdhandler(cmdfile)
        for cmd in cmd_list:
            # 必须stdin, stdout, stderr，否则命令不执行
            stdin, stdout, stderr = sshclient.exec_command(cmd)
            result = stdout.read()
            # 标准输出没有结果的情况有两种
            # 一是命令执行完本来就没有结果，比如sleep 20
            # 二是命令执行报错，stdout没有记过，sterr有结果
            if len(result) == 0 and len(stderr.read()) != 0:
                print("Exec error: %s" % stderr.read().decode('utf-8'))
            else:
                print("Result:%s" % result.decode('utf-8'))
    except Exception as e:
        print("Error: %s %s" % (host, e))
    else:
        sshclient.close()


def main():
    sevinfo = sevhandler('tomcat', 'config2.ini')
    for key, value in sevinfo.items():
        a = threading.Thread(target=ssh, args=('cmd.txt', value,))
        a.start()
        # ssh(value)


if __name__ == '__main__':
    # start_time = time.time()
    main()
    # print("执行时间：%s" % (time.time() - start_time))
