import os
import fnmatch


def is_file_match(filname, patterns):
    """
    判断函数是否符合判断条件
    :param filname: 判断的文件名
    :param patterns: 判断的条件
    :return: 符合返回True，不符合则返回False
    """
    for pattern in patterns:
        if fnmatch.fnmatch(filname, pattern):
            return True
    return False


def find_files(dirs, patterns=['*'], exlude_dirs=[]):
    """
    找文件
    :param dirs: 需要寻找文件的目录
    :param patterns: 匹配的文件模式列表，默认为“*”通配符，表示所有的文件
    :param exlude_dirs: 需要排除的目录列表，默认为空列表，表示默认无需排除目录
    :return: 返回符合条件文件
    """
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dirs)):
        for i in exlude_dirs:
            if i in dirnames:
                dirnames.remove(i)
        for file in filenames:
            if is_file_match(file, patterns):
                # 一次return只能返回第一个符合要求的
                yield os.path.join(dirpath, file)


# 查找目录下所有的文件
# for i in find_files('.'):
#     print(i)

# 查找目录下的所有图片
# patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
# for i in find_files('/root/test/t', patterns):
#     print(i)

# 查找目录下除了5目录以外的其他目录下的所有图片
# patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
# exclude_dirs = ['3']
# for i in find_files('/root/test/t', patterns, exclude_dirs):
#     print(i)

# 查找目录下最大的是个文件
# 先找出该目录下的所有文件
# 通过字典生成式，生成键值对为文件名和文件大小的字典
files = {name: os.path.getsize(name) for name in find_files('/root/test/t')}
# items() 函数以列表形式返回可遍历的(键, 值) 元组数组
# sorted排序，用items()返回列表的第二个值进行降序排序，并取前十个
result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中,默认下标从0开始，可以传参指定下标起始位置
for i,t in enumerate(result, 1):
    print(i, t[0], t[1])


# 查找目录下最老的十个文件,getmtime获取的unix时间戳，值越小说明越老
files = {name: os.path.getmtime(name) for name in find_files('/root/test/t')}
result = sorted(files.items(), key=lambda d: d[1])[:10]
for i,t in enumerate(result, 1):
    print(i, t[0], t[1])


# 删除目录下的所有图片，及txt文件，除了其下的3目录
files = [name for name in find_files('/root/test/t', patterns=['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff', '*.txt'],
                                     exlude_dirs=['3'])]
for file in files:
    os.remove(file)