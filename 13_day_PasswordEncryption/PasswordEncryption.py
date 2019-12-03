import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password, salt=None):
    if salt is None:
        # 随机生成8个字节的字符串，作为随机密码key使用
        salt = os.urandom(8)
    if isinstance(salt, str):
        # 将字符串编码成字节，才能加密
        salt = salt.encode('utf-8')
    # 密码编码成字节
    password = password.encode('utf-8')
    # 第一个参数是密钥key(必须是bytes)，第二个参数是待加密的字符串(必须是bytes)，第三个参数是hash函数
    # digest()ascii格式显示
    # hexdigest()十六进制显示
    result1 = HMAC(salt, password, sha256).digest()
    result2 = HMAC(salt, password, sha256).hexdigest()
    return result1, result2


print(encrypt_password('123456'))
