"""搜索目录下的文件，并获取占用的磁盘空间"""
import os


# files = [i for i in os.listdir('/usr/lib/firmware') if i.endswith('.bin')]
# # os.path.getsize获得是文件的占用空间，单位是字节
# sum_size = sum(os.path.getsize(os.sep.join(['/usr/lib/firmware', i])) for i in files)
# print("%s 字节" % sum_size)

a = """Traceback (most recent call last):
  File "E:/python_project/everyday_python/24_Devops/Sec_4/4.1/test_string1.py", line 5, in <module>
    files = [i for i in os.listdir('/usr/lib/firmware') if i.endswith('.bin')]
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: '/usr/lib/firmware'"""

print(a.find("files"))