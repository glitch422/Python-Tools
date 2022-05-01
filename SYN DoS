from scapy.all import *
from scapy.layers.inet import TCP, IP, sr, ICMP
from scapy.layers.l2 import ARP, Ether, srp1

IPd = input("Please insert your target's IP address:\t")
IPs = input('Please insert your IP address:\t')
MACs = input('Please insert source MAC address:\t')
port = input("Please insert your target's port address:\t")
FIN = Ether(src=MACs)/IP(src=IPs, dst=IPd)/TCP(sport=RandShort(), dport=port, flags=1)
SYN = Ether(src=MACs)/IP(src=IPs, dst=IPd)/TCP(sport=RandShort(), dport=port, flags=2)
ACK = Ether(src=MACs)/IP(src=IPs, dst=IPd)/TCP(sport=RandShort(), dport=port, flags=16)
while True:
    try:
        replay, error = sr1(FIN, timeout=0.5, verbose=0)
        if replay:
            replay, error = sr1(SYN, timeout=0.5, verbose=0)
            if replay:
                replay, error = sr1(ACK, timeout=0.5, veerbose=0)
                continue
    except Exception as e:
        print(e)
        break
        
# GLITCH422
