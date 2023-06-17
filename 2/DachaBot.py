from bs4 import BeautifulSoup
import random
import requests
a = input()
response = requests.get(f'https://store.steampowered.com/category/{a}').content
html = BeautifulSoup(response, 'html.parser')
fact = random.choice(html.find_all(class_ = ))
print(fact.text)