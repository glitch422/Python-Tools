from scapy.all import *
from scapy.layers.inet import TCP, IP, sr, ICMP
from scapy.layers.l2 import ARP, Ether, srp1
import paramiko
import ftplib
import socket

ask = input('Do you want to insert domain, Net address or IP address?:\t')

def SSH_connection():
    username = input('Please insert the user name:\t')
    password = input('Please insert the password:\t')
    ip = input("Please insert the IP address to communication:\t")
    port = 22

    try:
        ssh_session = paramiko.SSHClient()
        ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_session.connect(ip, port, username, password)
        print(f'Login success!\nUsername: {username} , Password: {password}')
        while True:
            command = input('Insert a command to execute on the server:\t')
            stdin, stdout, stderr = ssh_session.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())
            end = input('Do you want to finish y/n?\t').lower()[0]
            if end == 'y':
                break
    except Exception as e:
        print(e)

def FTP_connection():
    ip = input('Insert IP address for connection:\t')
    username = input('Enter username:\t')
    password = input('Enter password:\t')

    try:
        session = ftplib.FTP()
        session.connect(f'{ip}', 21)
        session.login(username, password)
        print(f'Login success!\nUsername: {username} , Password: {password}')
        print('=====================================================')
        while True:
            command = input('Please choose the command (dir, pwd, get, put, cwd, or exit to close):\t').lower()
            if command == "pwd":
                print('================================================================')
                print(f'The working directory is -------> {session.pwd()}\n')
                print('=====================================================')
            elif command == 'dir':
                print('================================================================')
                print('The files of the directory is:\n')
                session.dir()  # It print itself the output
                print('=======================================================')
            elif command == "put":
                print('================================================================')
                file_upload = input('Enter the file that you would like to upload:\t')
                put_file = open(file_upload, 'rb')
                file_up_name = input('How would you like save the file in the server?\t')
                session.storbinary(f'stor {file_up_name}', put_file)
                put_file.close()
                print('==========================================================')
            elif command == 'get':
                print('================================================================')
                session.dir()
                file_download = input('Choose the file you want to download from the server:\t')
                get_file = open(file_download, 'wb')
                file_down_name = input('How would you like save the file in your computer?\t')
                session.retrbinary(f'retr {file_down_name}', get_file.write)
                get_file.close()
                print('================================================================')
            elif command == 'cwd':
                print('================================================================')
                print(f'The working directory is -------> {session.pwd()}\n')
                change_directory = input('Which directory would you like to go to?\t')
                session.cwd(change_directory)
                print(f'The working directory is -------> {session.pwd()}\n')
                print('================================================================')
            elif command == exit:
                print('The session is closed ...')
                session.close()
                break
            else:
                print("Wrong Command ...")
                ask = input('Would you like to exit y/n?\t').lower()[0]
                if ask == 'y':
                    print('The session is closed ...')
                    session.close()
                    break
                else:
                    continue
    except ftplib.error_perm:
        print(f'Wrong Credentials\n Username:{username} , Password:{password}')

def FTP_connection_anonymous():
    ip = input('Insert IP address for connection:\t')
    username = 'anonymous'
    password = ''

    try:
        session = ftplib.FTP()
        session.connect(f'{ip}', 21)
        session.login(username, password)
        print(f'Login success!\nUsername: {username} , Password: {password}')
        print('=====================================================')
        while True:
            command = input('Please choose the command (dir, pwd, get, put, cwd, or exit to close):\t').lower()
            if command == "pwd":
                print('================================================================')
                print(f'The working directory is -------> {session.pwd()}\n')
                print('=====================================================')
            elif command == 'dir':
                print('================================================================')
                print('The files of the directory is:\n')
                session.dir()  # It print itself the output
                print('=======================================================')
            elif command == "put":
                print('================================================================')
                file_upload = input('Enter the file that you would like to upload:\t')
                put_file = open(file_upload, 'rb')
                file_up_name = input('How would you like save the file in the server?\t')
                session.storbinary(f'stor {file_up_name}', put_file)
                put_file.close()
                print('==========================================================')
            elif command == 'get':
                print('================================================================')
                session.dir()
                file_download = input('Choose the file you want to download from the server:\t')
                get_file = open(file_download, 'wb')
                file_down_name = input('How would you like save the file in your computer?\t')
                session.retrbinary(f'retr {file_down_name}', get_file.write)
                get_file.close()
                print('================================================================')
            elif command == 'cwd':
                print('================================================================')
                print(f'The working directory is -------> {session.pwd()}\n')
                change_directory = input('Which directory would you like to go to?\t')
                session.cwd(change_directory)
                print(f'The working directory is -------> {session.pwd()}\n')
                print('================================================================')
            elif command == exit:
                print('The session is closed ...')
                session.close()
                break
            else:
                print("Wrong Command ...")
                ask = input('Would you like to exit y/n?\t').lower()[0]
                if ask == 'y':
                    print('The session is closed ...')
                    session.close()
                    break
                else:
                    continue
    except ftplib.error_perm:
        print(f'Wrong Credentials\n Username:{username} , Password:{password}')

def scanner():
    for port in range(0, 65536):
        x = (IP(dst=ip)/TCP(dport=[port], flags="S"))
        rec, wrong = sr(x, timeout=timeout, verbose=0)
        if rec:
            data = "{}".format(rec[0]).split(" ")[7][6:]
            print("Port {} up, Protocol = TCP, Service = {}".format(port, data))
            if port == 22:
                q1 = input("Do you want to connect?\t")
                if q1 == 'Yes' or q1 == 'yes' or q1 == 'YES':
                    SSH_connection()
                    continue
                elif q1 == 'No' or q1 == 'no' or q1 == 'NO':
                    print('Wrong Parameter!')
                    continue
                else:
                    print('Wrong Parameter!')
                    continue
            elif port == 21:
                q1 = input("Do you want to connect?\t")
                if q1 == 'Yes' or q1 == 'yes' or q1 == 'YES':
                    q2 = input('Do you want connect with user or with anonymous user:\t')
                    if q2 == 'user':
                        FTP_connection()
                        continue
                    elif q2 == 'anonymous user':
                        FTP_connection_anonymous()
                        continue
                    else:
                        print('Wrong Parameter!')
                        continue
                elif q1 == 'No' or q1 == 'no' or q1 == 'NO':
                    print('Wrong Parameter!')
                    continue
                else:
                    print('Wrong Parameter!')
                    continue
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
