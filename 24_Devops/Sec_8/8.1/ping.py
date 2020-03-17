import subprocess
# 使用subprocess模块，开启子进程来执行相应的脚本来完成这个操作，可以 获取其标准输入、标注输出、标准错误以及返回码
import threading

def is_reacheable(ip):
    """新版python 3.5中，建议采用run的方法
    stdout=subprocess.DEVNULL避免命令的输出在屏幕上
    """
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("{0} is alive".format(ip))
    else:
        print("{0} is not alive".format(ip))


def main():
    with open("ips.txt") as f:
        lines = f.readlines()
    # 注意这边读取文件的时候，为将换行符读取出来，这样会导致ping不成功，需要清除后面的换行符
    for line in lines:
        t = threading.Thread(target=is_reacheable, args=(line.strip('\n'), ))
        t.start()


if __name__ == '__main__':
    main()