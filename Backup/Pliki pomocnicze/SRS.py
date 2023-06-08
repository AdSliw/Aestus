import speech_recognition as sr
import pyttsx3 as tts
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def mow(text):
    engine.say(text)
    engine.runAndWait()

def trueintro():
    print ('\n' + 'Aby sprawdzic dostepnosc torow wybierz 1.\nAby umowic sie na zejcia z instruktorem wybierz 2.\nAby zarezerwowac tor wybierz 3.\nAby otworzyc grafik wybierz 4.\nAby otworzyc strone internetowa basenu wybierz 5.\nAby otworzyc panel administratora wybierz 6.' + '\n')
    print('Co chcesz zrobic(1,2,3,4,5,6)?' + '\n' + 'Wypowiedz numer 1:')
    mow('Co chcesz zrobic(1,2,3,4,5,6)?')
    print('Slucham...')
    intro()

def intro():
    wybor = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
            mow(wybor_audio)
        except:
            print(end='.')
            intro()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            wybor = str(1)
        elif wybor_audio == '1':
            wybor = str(1)
        elif wybor_audio == '2':
            wybor = str(2)
        elif wybor_audio == '3':
            wybor = str(3)
        elif wybor_audio == '4':
            wybor = str(4)
        elif wybor_audio == 'pięć':
            wybor = str(5)
        elif wybor_audio == '5':
            wybor = str(5)
        elif wybor_audio == '6':
            wybor = str(6)
        else:
            intro()
        print ('\n' + 'Wybrales numer: '+ wybor + '\n')
        if wybor == str(1):
            print('\n' + 'Chcesz sprawdzic dostepnosc torow.')
            print('dobrze')
            intro()
        if wybor == str(2):
            print('\n' + 'Chcesz zamowic zajecia z instruktorem.')
            intro()
        if wybor == str(3):
            print('\n' + 'Chcesz zarezerowac tor.')
            intro()
        if wybor == str(4):
            print('\n' + 'Chcesz otworzyc grafik.')
            intro()
        if wybor == str(5):
            print('\n' + 'Chcesz otworzyc strone internetowa basenu.')
            intro()
        if wybor == str(6):
            print('\n' + 'Otwieranie panelu administratora.')
            intro()
        else:
            print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
            intro()
trueintro()
