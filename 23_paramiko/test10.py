"""批量上传及下载文件
两种方法：
1：扫描远端目录下所有文件及子目录下的文件，组合文件完整路径，逐一下载，
但是这种方法需要在本地创建每个子级目录，存在bug，较为繁琐
2: 判断远端是目录还是文件，文件就自己下载，目录的话，直接传递打包命令，
然后下载打包后的文件即可。
"""
import paramiko
import configparser
import os
import stat
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


class TransportClient(object):
    def __init__(self, hostname, port=22, username='root', pwd='123456'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.pwd = pwd
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.pwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        self.sshclient = paramiko.SSHClient()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(hostname=self.hostname,
                               port=self.port,
                               username=self.username,
                               password=self.pwd)

    def uploadfile(self, local_path, remote_path):
        # 如果本地上传的是一个目录，目的也是一个目录
        if os.path.isdir(local_path):
            # 扫描获取目录中的文件
            filelist = os.listdir(local_path)
            # 远程木服务器创建此目录
            stdin, stdout, stderr = self.sshclient.exec_command('mkdir -p %s' % remote_path[0:-1])
            for file in filelist:
                # 获取本地文件的完整路径
                localfile = os.sep.join([local_path[0:-1], file])
                # 获取目的文件的完整路径
                remotefile = os.sep.join([remote_path[0:-1], file])
                self.sftp.put(localfile, remotefile)
        # 如果本地上传的是一个文件
        else:
            # 且目的地是一个目录，以'/'结尾
            if remote_path[-1] == '/':
                # 获取本地文件名
                localdir, filename = os.path.split(local_path)
                # 生成远程文件完整路径
                remotefile = os.sep.join([remote_path[0:-1], filename])
                self.sftp.put(local_path, remotefile)
            # 目的地是完整文件路径
            else:
                self.sftp.put(local_path, remote_path)

    def __get_all_remote_file(self, remote_path):
        all_files = list()
        # 去掉路径字符串最后的字符“/”，如果有的话
        if remote_path[-1] == '/':
            remote_path = remote_path[0:-1]
        # listdir查看目录下文件以及子目录(不会列出子目录里面的内容),无法区分返回的是文件夹还是文件
        # listdir_attr 返回更加细粒度的文件信息，能够通过stat模块，判断文件是文件夹还是文件
        # 返回的是一个FSTPAttributes对象，包括文件的inde、拥有者、拥有组等详细信息
        remotefiles = self.sftp.listdir_attr(remote_path)
        for i in remotefiles:
            # 生成remote_dir目录下每一个文件或者目录的完整路径
            filename = os.sep.join([remote_path, i.filename])
            # 如果此文件仍是目录，就递归处理该目录，直到处理到最后一级不是目录
            # stat库中的S_ISDIR方法能够根据上面返回的详细信息中的mode,判断其是否是目录
            if stat.S_ISDIR(i.st_mode):
                # 将子目录下的文件列出的列表扩展到总的列表上
                all_files.extend(self.__get_all_remote_file(filename))
            # 如果判断此文件不是目录,则添加到总列表中
            else:
                all_files.append(filename)
        return all_files

    def download(self, remote_path, local_path):
        # 获取远端目录下所有的文件及子目录下的文件
        all_files = self.__get_all_remote_file(remote_path)
        if not os.path.exists(local_path):
            os.mkdir(local_path[0:-1])
        for i in all_files:
            filename = i.split('/')[-1]
            local_filename = os.sep.join([local_path[0:-1], filename])
            self.sftp.get(i, local_filename)


if __name__ == '__main__':
    client = TransportClient('192.168.6.166')
    client.download('/tmp/', 'test2/')










