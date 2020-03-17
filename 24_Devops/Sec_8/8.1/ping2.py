"""
每个ip都会创建一个线程，如果ip过多，创建太多进程，会导致问题，所以需要尽量控制
进程的数量，这里采用线程池的方法控制
"""
from concurrent.futures import ThreadPoolExecutor
import subprocess
import time


def is_reacheable(ip):
    """新版python 3.5中，建议采用run的方法"""
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print("{0} is alive".format(ip))
    else:
        print("{0} is not alive".format(ip))


def main():
    # 打开一个线程对象，最大容量为5
    with ThreadPoolExecutor(max_workers=5) as t:
        with open("ips.txt") as f:
            lines = f.readlines()
        for line in lines:
            t.submit(is_reacheable, line.strip('\n'))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("耗时:{0}".format(time.time()-start_time))