import requests

url = 'https://www.skelbiu.lt/users/signin'
payload = {'nick': '', 'password':''} #Fill in with account name and password

with requests.Session() as s:
    p = s.post(url, data=payload)

    url2='https://www.skelbiu.lt/users/renew'
    payload2= {'command': 'renew'}
    s.post(url2, data=payload2)
    

