import os
import fnmatch


# dir = '/usr/local/python3'
#
# for dirpath, dirnames, filenames in os.walk(dir):
#     print(dirpath)
#     print("*" * 50)
#     print(dirnames)
#     print("*" * 50)
#     print(filenames)
#     print(">" * 50)

# 后缀列表
images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []
# os.walk会遍历目录下的所有目录，包括父目录和子目录
# 每遍历一次返回三元组，第一个保存到是当前目录，第二个保存的当前目录下的子目录列表，第三个保存的是当前目录下的文件列表
for dirpath, dirnames, filenames in os.walk(os.path.expanduser('~/test/t')):
    # 遍历后缀列表
    for extensions in images:
        # filter过滤当前目录下的所有文件，找到符合当前后缀的文件
        for filename in fnmatch.filter(filenames, extensions):
            # 添加符合条件的文件
            matches.append(os.path.join(dirpath, filename))

print(matches)