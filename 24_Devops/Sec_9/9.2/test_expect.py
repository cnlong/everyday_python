import pexpect

# spawn启动scp程序
child = pexpect.spawn('scp README.txt root@192.168.6.163:/root/')

# expect方法等待子进程产生的输出，判断是否匹配期望的字符串
child.expect("root@192.168.6.163's password:")

# 匹配到期望的字符串以后，发送密码串作为输入
child.sendline('271138425')