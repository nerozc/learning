import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
date = 'date_req=13/02/2023'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req': today}

response = requests.get(url, payload)
loh = 'Евро'
xml = BeautifulSoup(response.content, 'lxml')
rub_eur = xml.find({'name':loh}).value.text.replace(',','.')

print(rub_eur)