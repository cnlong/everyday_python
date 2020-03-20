from scapy.all import *

# sniff(filter="icmp", prn=lambda x: x.summary(), count=10)
sniff(filter="host www.baidu.com", prn=lambda x: x.summary(), count=10)