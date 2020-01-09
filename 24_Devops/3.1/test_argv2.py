from __future__ import print_function
import sys
import os


def main():
    # 如果直接不加任何参数的运行，此时列表里面只有一个元素（程序本身）
    # 取sys.argv[1]的时候，会报错索引越界
    # 如果加参数运行，会先默认将参数添加到argv列表中，然后再添加那个空元素，所有参数的索引必定从1开始
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        # 抛出异常，并退出解释器
        raise SystemExit(filename + ' does not exists')
    # 判断该文件是否有读的权限
    elif not os.access(filename, os.R_OK):
        raise  SystemExit(filename + ' is not accessible')
    else:
        print(filename + ' is accessible')
    print(sys.argv)


if __name__ == '__main__':
    main()