'''
这道题给了一串不知所云的字符串和一张写着"K->M、O->Q、E->G"的图片
分析图片发现，K->M、O->Q、E->G，都是隔了一个字符，错开对应
初步分析，给的字符串通过"K->M、O->Q、E->G"这样的错开关系对应翻译
A、B、C、D、E、F、G、H、I、J、K、L、M、N、O、P、Q、R、S、T、U、V、W、X、Y、Z
C、D、E、F、G、H、I、J、K、L、M、N、O、P、Q、R、S、T、U、V、W、X、Y、Z、A、B
'''

import string


# text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
text = 'map'
"""
# new_text = ''
# for i in text:
#     if ord(i) >= ord('a') and ord(i) <= ord('z'):
#         new_text += chr((ord(i) + 2 - ord('a') )% 26 + ord('a'))
#     else:
#         new_text += i
# print(new_text)
"""
# str.maketrans方法的作用，用于创建字符映射的转换表
# 当传入两个参数的时候，两个参数的长度必须一致，参数1中每一个位置上的字符对应于参数2中相同位置上的字符，并返回一个字符对应关系的字典
# 返回的结果相对于一个翻译本，再将需要翻译的字符用translate方法进行转换翻译即可
table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(table)
print(text.translate(table))
