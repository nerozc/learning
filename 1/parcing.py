from tkinter import *
window = Tk()
window.geometry('1600x900')
window.title('Фотоальбом')
def photo1_press():
    photo = PhotoImage(file='images\skelet.gif')
    label = Label(image=photo)
    label.image = photo
    label.place(width=1600,height=900,x = 0, y = 0)
    button_exit = Button( text='Выход',command= get_quit,bg='black',fg='white',font=('Ariel',40),)
    button_exit.place(x=1200,y=700,height=100,width=400)

def photo2_press():
    photo = PhotoImage(file='images\image2.gif')
    label = Label(image=photo)
    label.image = photo
    label.place(width=1600,height=900,x = 0, y = 0)
    button_exit = Button( text='Выход',command= get_quit,bg='black',fg='white',font=('Ariel',40),)
    button_exit.place(x=1200,y=700,height=100,width=400)
def photo3_press():
    photo = PhotoImage(file='images\image3.gif')
    label = Label(image=photo)
    label.image = photo
    label.place(width=1600,height=900,x = 0, y = 0)
    button_exit = Button( text='Выход',command= get_quit,bg='black',fg='white',font=('Ariel',40),)
    button_exit.place(x=1200,y=700,height=100,width=400)
def get_quit():
    window.destroy()
def close_window():
    pass
button_1 = Button(text='Фото',command= photo1_press,bg='black',fg='white',font=('Ariel',40),)
button_1.place(x=50,y=200,height=100,width=400)
button_exit = Button( text='Выход',command= get_quit,bg='black',fg='white',font=('Ariel',40),)
button_exit.place(x=1200,y=700,height=100,width=400)
button_2 = Button(text='Фото 2',command= photo2_press,bg='black',fg='white',font=('Ariel',40),)
button_2.place(x=550,y=200,height=100,width=400)
button_3 = Button(text='Фото 3',command= photo3_press,bg='black',fg='white',font=('Ariel',40),)
button_3.place(x=1000,y=200,height=100,width=400)
window.protocol('WM_DELETE_WINDOW', close_window)
window.mainloop()