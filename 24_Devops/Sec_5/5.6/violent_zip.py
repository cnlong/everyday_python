# 暴力破解zip文件
import zipfile


f = zipfile.ZipFile('example.zip')
with open('password.txt') as pwds:
    for line in pwds:
        try:
            f.extract(pwd=line.strip())
            print("password is {0}".format(line.strip()))
        except:
            print("password is not correct")
