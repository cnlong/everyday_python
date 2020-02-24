# 备份所有的图片到压缩包中
import os
import fnmatch
import tarfile
import datetime


def is_file_match(filename, patterns):
    """
    判断文件是否符合条件
    :param filename: 文件名
    :param patterns: 条件列表
    :return: 返回True os False
    """
    for i in patterns:
        if fnmatch.fnmatch(filename, i):
            return True
        return False


def find_file(directory, patterns=['*'], exlude_dirs=[]):
    """
    找到所有符合条件的文件
    :param directory: 遍历的目录
    :param patterns: 条件。默认是星号，所有文件
    :param exlude_dirs: 需要排除的目录，默认为空
    :return: 返回找到的文件
    """
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(directory)):
        for i in exlude_dirs:
            if i in dirnames:
                dirnames.remove(i)
        for file in filenames:
            if is_file_match(file):
                yield os.path.join(dirpath, file)


def main():
    # 定义判断条件
    patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    # 获取当前时间
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = "all_images_{0}.tar.gz".format(now)
    with tarfile.open(filename, mode='w:gz') as f:
        for item in find_file(".", patterns):
            f.add(item)


if __name__ == '__main__':
    main()