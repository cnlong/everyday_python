import os


# 获取当前用户home目录下的所有文件列表
print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isfile(os.path.join(os.path.expanduser('~'), item))])

# 获取当前用户home目录下所有的目录列表
print([item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(os.path.join(os.path.expanduser('~'), item))])

# 获取字典
print({item: os.path.realpath(item) for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(os.path.join(os.path.expanduser('~'), item))})