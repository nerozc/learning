import speech_recognition
import wave 
import json 
import os  
if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    ttsEngine = pyttsx3.init()
    while True:
        voice_input = record_and_recognize_audio()
        print(voice_input)
def record_and_recognize_audio(*args: tuple):

    with microphone:
        recognized_data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("слухаю")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("включил говорилку?")
            return
        try:
            print("распознаю епта")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("офни ебальник")
        return recognized_data