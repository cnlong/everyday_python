import os
import hmac
import hashlib


a = os.urandom(8)
print(a)
# 第一个参数是密钥key(必须是bytes)，第二个参数是待加密的字符串(必须是bytes)，第三个参数是hash函数
a = 'salt'
b = 'hahaha'
a = a.encode('utf-8')
b = b.encode('utf-8')
mac = hmac.new(a, b, hashlib.md5)
# 打印出加密后字符串的ascii格式
print(mac.digest())
# 打印出加密后字符串的十六进制格式
print(mac.hexdigest())