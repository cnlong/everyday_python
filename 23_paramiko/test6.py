import paramiko


transport = paramiko.Transport(('192.168.6.166', 22))
transport.connect(username='root', password='123456')
# 创建SFTP实例,并指定连接的对象
sftp = paramiko.SFTPClient.from_transport(transport)
# 上传文件，参数为本地文件路径，和远程文件路径
# get或put方法每次只能传输一个文件，而不是整个目录
sftp.put('client.txt', '/tmp/client.txt')
# 下载文件.参数为远程文件路径，和本地文件路径
sftp.get('/tmp/server.txt', 'server.txt')
transport.close()

