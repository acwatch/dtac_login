import requests

#Dtac URL
url = 'https://wifilogin.dtacbroadband.co.th/ssportal6/login.do'
post_data = {'userName': 'xxxxxxxxxx', #telephone no.
            'password': 'xxxx'} #pass
print requests.post(url, data=post_data).text
