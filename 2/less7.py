import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import random
r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я голосовй помощник')
voice.runAndWait()
list_film = ['Зеленая миля', 'Список Шиндлера', 'Побег из Шоушенка', 'Форрест Гамп']
while True:
    with sr.Microphone(device_index = 1) as source:
        print('Скажите что-нибудь')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language = 'ru_RU').lower()
    print(speech)
    if speech.find('фильм') >=0:
        voice.say(random.choice(list_film))
        voice.runAndWait()
    elif speech.find('youtube')>=0:
        webbrowser.open_new('https://www.youtube.com')
        voice.say('Открываю эту ебучую вкладку')
        voice.runAndWait()
    elif speech.find('файл') >=0:
        os.startfile('file.txt')
        voice.say('Открываю этом ебучий файл')
        voice.runAndWait()
    elif(speech.find('пока') >=0):
        voice.say('Пока, кожанный')
        voice.runAndWait()
        break
    else:
        voice.say('Я тебя не понимаю, кожанный')
        voice.runAndWait()