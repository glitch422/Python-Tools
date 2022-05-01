from scapy.all import *
from scapy.layers.inet import TCP, IP, sr, ICMP
from scapy.layers.l2 import ARP, Ether, srp1

net = input('Please enter your network address:\t')
net_split = net.split('.')
mask = input('Please enter netmask for scanning:\t')
if mask == '0.0.0.0':
    for host in range(256):
         ip = f'{host}.{host}.{host}.{host}'
         arpReq = Ether(dest='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff') 
         arpRes = srp1(arpReq, timeout=0.5, verbose=0) 
         print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
elif mask == '255.0.0.0':
    for host in range(256):
         ip = f'{net_split[0]}.{host}.{host}.{host}'
         arpReq = Ether(dest='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff') 
         arpRes = srp1(arpReq, timeout=0.5, verbose=0) 
         print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
elif mask == '255.255.0.0':
    for host in range(256):
        ip = f'{net_split[0]}.{net_split[1]}.{host}.{host}'
        arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
        arpRes = srp1(arpReq, timeout=0.5, verbose=0)
        print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
elif mask == '255.255.255.0':
    for host in range(256):
        ip = f'{net_split[0]}.{net_split[1]}.{net_split[2]}.{host}'
        arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
        arpRes = srp1(arpReq, timeout=0.5, verbose=0)
        print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
else:
    print('Error!')
    
# Glitch422
