"""
创建类似xshell的功能，登录以后可以输入命令回车后就返回结果
"""
import paramiko
import sys
import select

trans = paramiko.Transport(('192.168.6.166', 22))
# 启动客户端
trans.start_client()
# 密码认证登录
trans.auth_password(username='root', password='123456')
# 打开一个通道
channel = trans.open_session()
# 获取终端
channel.get_pty()
# 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
channel.invoke_shell()
# 下面就可以执行你所有的操作，用select实现
# 对输入终端sys.stdin和 通道进行监控,
# 当用户在终端输入命令后，将命令交给channel通道，这个时候sys.stdin就发生变化，select就可以感知
# channel的发送命令、获取结果过程其实就是一个socket的发送和接受信息的过程
while True:
    # readlist, writelist, errlist = select.select([channel, sys.stdin,], [], [])
    readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])
    # 如果用户输入命令，systdin发送变化
    if sys.stdin in readlist:
        # 获取输入内容
        input_cmd = sys.stdin.read(1)
        # 将命令发送给服务器
        channel.sendall(input_cmd)
    # 服务器返回了结果，select感知到chaanel通道变化，接收到结果
    if channel in readlist:
        # 获取结果
        result = channel.recv(1024)
        # 断开连接后，channel变化，但是接收到的值为0
        if len(result) == 0:
            print('结束连接')
            break
        # 输出到屏幕
        sys.stdout.write(result.decode())
        sys.stdout.flush()

# 关闭通道
channel.close()

# 关闭连接
trans.close()


