from scapy.all import *

target_ip = '192.168.6.230/24'

# 创建arp packet
ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=target_ip),timeout=2,verbose=False)
for snd,rcv in ans:
    list_mac = rcv.sprintf("%Ether.src% - %ARP.psrc%")
    print(list_mac)