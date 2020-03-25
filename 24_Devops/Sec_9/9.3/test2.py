import paramiko


def deploy_monitor(ip, username, password, filename, port=22):
    """
    部署文件的函数
    :param ip: 远程服务器Ip
    :param username: 登录用户名
    :param password: 密码
    :param port: 登录端口，默认22端口
    :return:
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port, username, password)
        print("{0} connect successful!".format(ip))
        sftp = client.open_sftp()
        sftp.put(filename, 'testfile3.txt')
        sftp.listdir('/root')
        print("{0} upload {1} successful".format(ip, filename))
    except Exception as err:
        raise SystemExit("{0} found!".format(err))


def main():
    username = input('请输入登录用户名：')
    passwd = input('请输入密码：')
    filename = input('请输入上传的文件名：')
    with open('hosts.txt') as f:
        # 注意读取出来的内容包括换行符，需要去除
        for host in f:
            deploy_monitor(host.strip('\n'), username, passwd, filename)


if __name__ == '__main__':
    main()