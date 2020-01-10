"""批量修改服务器密码"""
import paramiko
import configparser
import sys
import threading
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


def ssh(host, oldpwd, newpwd, port=22, username='root'):
    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.connect(hostname=host,
                          port=port,
                          username=username,
                          password=oldpwd)
        stdin, stdout, stderr = sshclient.exec_command('echo %s | passwd --stdin root' % newpwd)
        result = stdout.read()
        if len(result) == 0 and len(stderr.read()) != 0:
            print("%s exec error: %s" % (host, stderr.read().decode('utf-8')))
        else:
            print("%s exec success" % host)
    except:
        print("host %s connect failed" % host)
    else:
        sshclient.close()


def main():
    # newpasswd = input("请输入新密码: ")
    # newpasswd2 = input("请再次输入新密码: ")
    newpasswd = getpass.getpass("请输入新密码: ")
    newpasswd2 = getpass.getpass("请再次输入新密码: ")
    if newpasswd != newpasswd2:
        print("两次输入密码不一样，请重新运行并输入密码")
        sys.exit(1)
    sev_dict = sevhandler('prd', 'config3.ini')
    for key, value in sev_dict.items():
        host = value.split(',')[0]
        oldpwd = value.split(',')[1]
        a = threading.Thread(target=ssh, args=(host, oldpwd, newpasswd))
        a.start()


if __name__ == '__main__':
    main()