import datetime
import telebot
from bs4 import BeautifulSoup
import requests
response= requests.get('https://luna.titdang.me/')
response = response.content
html = BeautifulSoup(response, 'html.parser')
sex = html.find(class_ = 'item')
print(sex)