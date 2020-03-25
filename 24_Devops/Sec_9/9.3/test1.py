import paramiko

# 创建sshclient
client = paramiko.SSHClient()

# 设置自动添加服务器
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
client.connect('192.168.6.192', 22, 'root', '123456')

# 接收命令执行的三个channel
stdin, stdout, stderr = client.exec_command('ls -l')

# 打印输出结果
print(stdout.readlines())

# 创建SFTPClient
sftp = client.open_sftp()

# 上传文件
sftp.put('README.txt', 'hahah0324.txt')

# 查看文件信息
print(sftp.stat('hahah0324.txt'))

# 重命名
sftp.rename('hahah0324.txt', '0324.txt')

# 删除文件
sftp.remove('0324.txt')

# 关闭连接
sftp.close()
client.close()
