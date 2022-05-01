from scapy.all import *
from scapy.layers.inet import TCP, IP, sr, ICMP
from scapy.layers.l2 import ARP, Ether, srp1

ask = input('Do you want to insert domain, Net address or IP address?:\t')
def scanner():
    for port in range(0, 65536):
        x = (IP(dst=ip)/TCP(dport=[port], flags="S"))
        rec, wrong = sr(x, timeout=timeout, verbose=0)
        if rec:
            data = "{}".format(rec[0]).split(" ")[7][6:]
            print("Port {} up, Protocol = TCP, Service = {}".format(port, data))
        else:
            print(f'The port {port} is close')


if ask == 'domain':
    domain = input('Insert a domain for a scan:\t')
    ip = socket.gethostbyname(domain)
    timeout = int(input('Set the timeout of scanning:\t'))
    arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
    arpRes = srp1(arpReq, timeout=0.5, verbose=0)
    print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
    scanner()
elif ask == 'IP address':
    ip = input('Please enter your IP address:\t')
    timeout = int(input('Set the timeout of scanning:\t'))
    arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
    arpRes = srp1(arpReq, timeout=0.5, verbose=0)
    print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
    scanner()
elif ask == 'Net address':
    net = input('Please enter your network address:\t')
    net_split = net.split('.')
    mask = input('Please enter netmask for scanning:\t')
    timeout = int(input('Set the timeout of scanning:\t'))
    if mask == '0.0.0.0':
        for host in range(256):
            ip = f'{host}.{host}.{host}.{host}'
            arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
            arpRes = srp1(arpReq, timeout=0.5, verbose=0)
            print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
            scanner()
    elif mask == '255.0.0.0':
        for host in range(256):
            ip = f'{net_split[0]}.{host}.{host}.{host}'
            arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
            arpRes = srp1(arpReq, timeout=0.5, verbose=0)
            print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
            scanner()
    elif mask == '255.255.0.0':
        for host in range(256):
            ip = f'{net_split[0]}.{net_split[1]}.{host}.{host}'
            arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
            arpRes = srp1(arpReq, timeout=0.5, verbose=0)
            print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
            scanner()
    elif mask == '255.255.255.0':
        for host in range(256):
            ip = f'{net_split[0]}.{net_split[1]}.{net_split[2]}.{host}'
            arpReq = Ether(dest='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
            arpRes = srp1(arpReq, timeout=0.5, verbose=0)
            print(f'IP: {arpRes.psrc}, MAC : {arpRes.hwsrc}')
            scanner()
    else:
        print('Error!')
else:
    print('Error!')

# Glitch422
