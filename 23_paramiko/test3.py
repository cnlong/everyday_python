"""
创建类，封装ssh类，读取文件，保证密码安全
"""
import configparser
import paramiko

# config = configparser.ConfigParser()
# config.read('config.ini')
# host = config.get('ssh', 'host')
# port = int(config.get('ssh', 'port'))
# user = config.get('ssh', 'user')
# pwd = config.get('ssh', 'pwd')
# time = float(config.get('ssh', 'timeout'))
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # print('hostname={}, port={}, username={}, password={}, timeout={}'.format(host, port, user, pwd, time))
# ssh_client.connect(hostname=host, port=port, username=user, password=pwd, timeout=time)
# stdin, stdout, stderr = ssh_client.exec_command('hostname')
# print(stdout.read())


class SshClient(object):
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.host = self.config.get('ssh', 'host')
        self.port = self.config.get('ssh', 'port')
        self.user = self.config.get('ssh', 'user')
        self.pwd = self.config.get('ssh', 'pwd')
        self.timeout = self.config.get('ssh', 'timeout')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host,
                            port=int(self.port),
                            username=self.user,
                            password=self.pwd,
                            timeout=float(self.timeout)
                            )

    def run_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        result = stdout.read()
        # 输出结果长度为0即没有输出，表示有错误
        if len(result) == 0:
            print(stderr.read().decode('utf-8'))
        else:
            print(result.decode('utf-8'), end='')

    def client_close(self):
        self.client.close()


if __name__ == '__main__':
    ssh_client = SshClient('config.ini')
    ssh_client.run_command('hostname')
    ssh_client.client_close()
