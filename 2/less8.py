from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.title('app')
window.geometry('800x600')
count = 0
def changelable():
    global count
    count+=1
    lab['text'] = f'Кнопка нажата {count} раз'

lab = Label(window,text = 'Текст', bg = 'green', fg = 'black', font = '16')
lab.place(x=100,y=200)
btn = Button(text = 'Кнопка',background = 'black', foreground='white',font = '16', command = changelable)
btn.place(x=200,y=250)
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today()
today = today.strftime('%d/%m/%Y')
payload = {'date_req': today}

response = requests.get(url, payload)

xml = BeautifulSoup(response.content, 'lxml')

def getCourse(id):
    return xml.find('valute', {'id':id}).value.text
img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo)
logo.place(x=0,y=0)
cat_photo = PhotoImage(file='cat.png')
cat = Label(window, image=cat_photo)
cat.place(x=500,y=450)
a = getCourse('R01375')
lab = Label(window,text=f'Курс юаня\n{a}',font = 22)
lab.place(x=150,y=200)
window.resizable(width=False, height=False)
window.mainloop()