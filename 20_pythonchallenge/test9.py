# BZ开始的字符串实际是被bz2压缩后的一种格式
# compress是压缩函数，那么decompress就是解压函数
import bz2


content_un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
content_pw  = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
username = bz2.decompress(content_un).decode()
passwd = bz2.decompress(content_pw).decode()
print(username, passwd)