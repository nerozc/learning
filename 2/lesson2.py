import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
date = 'date_req=13/02/2023'

today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req': today}

response = requests.get(url, payload)

xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text
def exchange_rate(valute_from, valute_to, amount):
    eur = xml.find('valute',{'id':'R01239'}).value.text.replace(',','.')
    usd = xml.find('valute',{'id':'R01235'}).value.text.replace(',','.')

    if(valute_from == 'RUB'):
        return xml.find('valute',{'id':valute_from}).value.text.replace(',','.')*amount
    elif(valute_to =='RUB'):
        return float(xml.find('valute',{'id':valute_from}).value.text.replace(',','.'))*amount 
    elif(valute_from !='RUB '):
        return float(xml.find('valute',{'id':valute_from}).value.text.replace(',','.'))/ float(xml.find('valute',{'id':valute_from}).value.text.replace(',','.'))*amount
valute_from = input('Введите код валюты')
valute_to = input('Введите код валюты')
amount = int(input())

result = exchange_rate(valute_from,valute_to,amount)
print(round(result,1))