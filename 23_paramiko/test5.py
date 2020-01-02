"""
transport封装登录：是一种加密的会话，使用时会同步创建一个加密的Tunnels(通道)，这个Tunnels叫Channel
"""
import paramiko


# 创建通道transport对象，绑定主机和端口，指定用户和密码连接
transport = paramiko.Transport(('192.168.6.166', 22))
transport.connect(username='root', password='123456')

# 创建ssh会话实例
ssh = paramiko.SSHClient()
# 类属性赋值，指定transport,就无需再指定主机端口等参数
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('free -m')
print(stdout.read().decode('utf-8'))
ssh.close()