""""找到目录下的重复文件"""
import hashlib
import os
import fnmatch
import sys


# 设置读取的字节数
CHUNK_SIZE = 8192

def find_files(dirs):
    """
    根据条件找文件
    :param dirs: 目录名
    :param patterns: 条件，默认为“*”，找出所有文件
    :param exclude_dirs: 需要排除的文件，默认为空
    :return: 返回找到的文件
    """
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(dirs)):
        for i in filenames:
                yield os.path.join(dirpath, i)

def get_chunk(filename):
    """
    按块读取文件
    :param filename: 文件名
    :return: 返回读取的内容
    """
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            # 如果为空，退出循环
            if not chunk:
                break
            else:
                yield chunk


def get_file_checksum(filename):
    """
    获取文件的md5值
    :param filename:
    :return:
    """
    h = hashlib.md5()
    # 逐块获取更新文件的md5值
    for chunk in get_chunk(filename):
        h.update(chunk)
    return h.hexdigest()


def main():
    # 从命令行获取文件夹名称
    # 添加空元素，防止未添加参数时候，获取文件夹名称时候，索引超出范围
    sys.argv.append("")
    # 获取要操作的文件夹名称
    directory = sys.argv[1]
    # 判断该文件夹是否是文件夹，并且存在
    if not os.path.isdir(directory):
        raise SystemExit("{0} is not a directory".format(directory))
    # md5值和文件夹的字典
    record = dict()
    # 遍历文件夹，找出所有文件
    for item in find_files(directory):
        # 获取文件md5值
        checksum = get_file_checksum(item)
        # 判断该md5值是否在md5字典中
        if checksum in record:
            # 如果存在，说明有重复相同文件
            print('find duplicate file: {0} vs {1}'.format(record[checksum], item))
        else:
            # 如果不存在同样的Md5值，则加入md5字典中
            record[checksum] = item

if __name__ == '__main__':
    main()
