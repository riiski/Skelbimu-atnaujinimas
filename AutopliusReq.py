from lxml import html
import requests


url = 'https://autoplius.lt/pasas/registracija'
payload = {'login_name': '', 'login_password':'', 'is_login' : '1'} #Fill in with account name and password


with requests.Session() as s:
    p = s.post(url, data=payload) # connection request

    tree = html.fromstring(p.content)

    #find :renew: buttons
    ads = tree.xpath('//*[@class="submit-link center submit-grey fr"]//@href')
    atitinka = [l for l in ads if 'renew' in l]

    #request GET method for update
    for t in atitinka:
        s.get(t)