import paramiko
import os
from stat import *


def get_all_files_in_remote_dir(sftp, remote_dir, local_dir):
    # 保存所有文件的列表
    all_files = list()
    if not os.path.exists(local_dir):
        os.mkdir(local_dir)

    # 去掉路径字符串最后的字符'/'，如果有的话
    if remote_dir[-1] == '/':
        remote_dir = remote_dir[0:-1]

    # 获取当前指定目录下的所有目录及文件，包含属性值
    files = sftp.listdir_attr(remote_dir)
    for x in files:
        # remote_dir目录中每一个文件或目录的完整路径
        filename = remote_dir + '/' + x.filename
        # 如果是目录，则递归处理该目录，这里用到了stat库中的S_ISDIR方法，与linux中的宏的名字完全一致
        if S_ISDIR(x.st_mode):
            os.mkdir(local_dir + '/' + x.filename)
            all_files.extend(get_all_files_in_remote_dir(sftp, filename, local_dir))
        else:
            all_files.append(filename)
    return all_files


transport = paramiko.Transport(('192.168.6.166', 22))
transport.connect(username='root', password='123456')
# 创建SFTP实例,并指定连接的对象
sftp = paramiko.SFTPClient.from_transport(transport)
all_files = get_all_files_in_remote_dir(sftp, '/test', 'test')
local_dir = 'test'
for x in all_files:
    filename = x.split('/')[-1]
    local_filename = os.path.join(local_dir, filename)
    print('Get文件%s传输中...' % filename)
    sftp.get(x, local_filename)

transport.close()

# a = os.listdir('test')
# print(a)
# a, b = os.path.split('heloo/world.txt')
# print(a)
# print(b)
# c = '/usr/local/'
# print(c[-1])
# print(c[0:-1])
# a = 'hello/'
# b = 'nihao.txt'
# print(os.sep.join([a, b]))
# os.makedirs('test2/test1/test.txt/')
# sshclient = paramiko.SSHClient()
# sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# sshclient.connect(hostname='192.168.6.166', port=22, username='root', password='123456')
#
# stdin, stdout, stderr = sshclient.exec_command('mkdir /tmp/test')
# sshclient.close()
# print(os.stat('test'))