from tkinter import *

window = Tk()  # создание экземпляра класса Tk
window.geometry('700x500')
window.title('Тестирование на знание киновселенной Marvel')

facts = [
    {'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
    {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
    {'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
    {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
]
cur_q = 0
point = 0
label_title = Label(text='Marvel Test', font=('Arial',24),fg = 'white',bg = 'red')
label_title.place(width=700,height=50, x=0 ,y=0)
fact = Message(text=facts[cur_q]['text'],font = ('Arial',24), width= 680,)
fact.configure(justify=CENTER)
fact.place(x = 10, y = 70)
var = IntVar()
true = Radiobutton(text = 'Правда', variable=var,value = 1)
false = Radiobutton(text = 'Ложь', variable=var,value = 0)
true.place(x = 10, y = 120)
false.place(x = 100, y = 120)
window.mainloop()
