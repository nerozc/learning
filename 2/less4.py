import requests
import json
ship = ''
max_speed = 0
url = 'https://swapi.dev/api/'
response = requests.get(url).json()
starships_api = response.get('starships')
def starships(url):
    ship_list = []
    names = {}
    response_starships = requests.get(url).json()
    for i in response_starships.get('results'):
        names[i['name']] = i['max_atmosphering_speed']
    #for sub in names:
    #    for key in sub:
   #         if(key == 'n/a'):
     #           print('1')
     #       elif(key == '1000km'):
    #            print('2')
    result = {}
    for i in names.values():
        if i == 'n/a':
            del names[i] 
    print(names)
starships(starships_api)