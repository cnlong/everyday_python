import paramiko
"""
SSHClient：它的作用类似于Linux的SSH命令，是对SSH会话的一个类的封装，这个类封装了传输(Transport),通道(Channel)及SFTPClient建立的方法(open_sftp),通过用于执行远程命令。

SFTPClient：它的作用类似Linux的SFTP命令，是对SFTP客户端的一个类的封装。主要是实现对远程文件的操作，上传，下载，修改文件权限等操作。
"""

# 创建sshclient对象
ssh_client = paramiko.SSHClient()
# 允许将新人的主机自动加入到host_allow列表中，必须放在connect方法前面
# 　客户端第一次访问时，服务端会创建一个konw_host文件存下客户端key，上述方式实现自动将不是自己konw_host下保存的key自动加入到里面。
# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器，填入参数，主机名，端口，用户名，密码
ssh_client.connect(hostname='192.168.6.166', port=22, username='root', password='123456')
command = 'ls /usr/local'
# 执行命令，输出结果在stdout中，如果是错误则放在stderr中
stdin, stdout, stderr = ssh_client.exec_command(command)
# 因为网络传输过程中是字节传输，需要进行解码
result = stdout.read().decode('utf-8')
if len(result) == 0:
    print(stderr.read().decode('utf-8'))
else:
    print(result)
