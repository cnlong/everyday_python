"""使用密钥进行登录"""
import paramiko
# 本地生成公私钥文件，必须先将公钥文件传输到需要登录的服务器上
# 指定本地的私钥文件
pkey = paramiko.RSAKey.from_private_key_file('id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.6.165', port=22, username='root', pkey=pkey)
stdin, stdout, stderr = ssh.exec_command('hostname')
ssh.close()