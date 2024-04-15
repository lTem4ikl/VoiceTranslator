from tkinter import *
from googletrans import Translator
import speech_recognition as sr

# __________________________________________________
def soundRecording():
# Создаем объект Recognizer
    recognizer = sr.Recognizer()

    # Создаем объект Microphone для записи звука
    microphone = sr.Microphone()

    # Записываем звук с микрофона
    with microphone as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Распознаем текст с помощью Google Web Speech API
    try:
        text = recognizer.recognize_google(audio, language="en-US")

    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь")
    except sr.RequestError:
        print("Произошла ошибка при обращении к API")

    # Записываем распознанный текст в переменную
    recognized_text = text if text else ""

    # __________________________________________________

    translator = Translator()
    result = translator.translate(text, dest='ru')
    translated_text = result.text
    print(f'Перевод: {translated_text}\n')


# __________________________________________________

    # window = Tk()  
    # window.title("Переводчик")  
    # # window.wm_attributes('-alpha', 0.5)
    # window.geometry('100x50')
    # lbl = Label(window, text=translated_text)  
    # lbl.grid(column=0, row=0)  
    # window.mainloop()

    soundRecording()

if __name__ == '__main__':
    while True:
        try:
            soundRecording()
        except Exception as e: 
            print('<<<ERROR>>>')
            soundRecording()

# if __name__ == '__main__':
#     soundRecording()