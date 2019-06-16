from lxml import html
import requests

#connection information
url = 'https://autogidas.lt/mano-gidas/'
payload = {'vartotojovardas': '', 'slaptazodis':'', 'login' : 'Prisijungti', 'remember' : '1'} #Fill in with account name and password

with requests.Session() as s:
    p = s.post(url, data=payload) #login request
    tree = html.fromstring(p.content)

    #find :renew: buttons
    ads = tree.xpath('//*[@class="buttons"]//@href')
    atitinka = [l for l in ads if '/ad/action/renew-selected?ad_id=' in l]

    #use GET method to request update
    autogidas='https://autogidas.lt'
    for t in atitinka:
        s.get(autogidas + t)
