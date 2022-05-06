import requests

url = input('Please enter url to get page info:\t')
site = requests.get(f'{url}')
try:
    code = site.status_code
    print(f'The page status code is {code}')
    if code == 200:
        cont = site.text
        print(f"The site's HTML is:\n{cont}")
except Exception as e:
    print(e)
  
# GLITCH422
