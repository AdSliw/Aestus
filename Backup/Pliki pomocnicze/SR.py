import speech_recognition as sr
import pyttsx3 as tts
r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#for device_index in Microphone.list_working_microphones():
#    m = Microphone(device_index=device_index)
#    break
#else:
#    print("No working microphones found!")
#
def mow(text):
    engine.say(text)
    engine.runAndWait()
#    
#def getText():
#    with sr.Microphone() as source:
#        try:
#            print("Slucham...")
#            audio = r.listen(source)
#            text = r.recognize_google(audio, language='pl-PL')
#            print(text)
#            if text !="":
#                return text
#            return 0
#        except:
#            return 0
#def program_mowa():
#    txt = getText()
#    if not txt == 0:
#        print(txt)
#        mow(txt)
#    else:
#        print('Nie udalo sie rozpoznac mowy.')

def exit():
    print("koniec")

def mow(text):
    engine.say(text)
    engine.runAndWait()
    
def textparser():
    text = ''
    with sr.Microphone() as source:
        try:
            print("Slucham... masz 3 sekundy.")
            # wait for speech for a maximum of 3 seconds
            # listen to speech for a maximum of 3 seconds
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            text = r.recognize_google(audio, language='pl-PL')
            print(text)     
            if text == "jeden":
                print("Koniec czasu.")
                print("bylo 1")
                return 1
            elif text == "2":
                print("Koniec czasu.")
                print("bylo 2")
                return 2
            elif text == "3":
                print("Koniec czasu.")
                print("bylo 3")
                return 3
            elif text == "4":
                print("Koniec czasu.")
                print("bylo 4")
                return 4
            elif text == "pięć":
                print("Koniec 5.")
                print("bylo 5")
                return 5
            elif text == "6":
                print("Koniec czasu.")
                print(" bylo 6")
                return 6
            elif text == "7" or text == "siedem":
                print("Koniec czasu.")
                print("bylo 7")
                return 7
            elif text == "8" or text == "osiem":
                print("Koniec czasu.")
                print("bylo 8")
                return 8
            elif text == "9":
                print("Koniec czasu.")
                print("bylo 9")
                return 9
            elif text == "10":
                print("Koniec czasu.")
                print("bylo 10")
                return 10
            elif text == "11":
                print("Koniec czasu.")
                print("bylo 11")
                return 11
            elif text == "12":
                print("Koniec czasu.")
                print("bylo 12")
                return 12
            elif text == "13":
                print("Koniec czasu.")
                print(" bylo 13")
                return 13
            elif text == "14":
                print("Koniec czasu.")
                print("bylo 14")
                return 14
            elif text == "15":
                print("Koniec czasu.")
                print("bylo 15")
                return 15
            elif text == "16":
                print("Koniec czasu.")
                print("bylo 16")
                return 16
            elif text == "17":
                print("Koniec czasu.")
                print("bylo 17")
                return 17
            elif text == "18":
                print("Koniec czasu.")
                print("bylo 18")
                return 18
            elif text == "19":
                print("Koniec czasu.")
                print(" bylo 19")
                return 19
            elif text == "20":
                print("Koniec czasu.")
                print("bylo 20")
                return 20
            elif text == "21":
                print("Koniec czasu.")
                print("bylo 21")
                return 21
            elif text == "22":
                print("Koniec czasu.")
                print("bylo 22")
                return 22
            elif text == "23":
                print("Koniec czasu.")
                print("bylo 23")
                return 23
            elif text == "24":
                print("Koniec czasu.")
                print("bylo 24")
                return 24
            elif text == "25":
                print("Koniec czasu.")
                print("bylo 25")
                return 25
            elif text == "26":
                print("Koniec czasu.")
                print(" bylo 26")
                return 26
            elif text == "27":
                print("Koniec czasu.")
                print("bylo 27")
                return 27
            elif text == "28":
                print("Koniec czasu.")
                print("bylo 28")
                return 28
            elif text == "29":
                print("Koniec czasu.")
                print(" bylo 29")
                return 29
            elif text == "30":
                print("Koniec czasu.")
                print("bylo 30")
                return 30
            elif text == "31":
                print("Koniec czasu.")
                print("bylo 31")
                return 31
            elif text == "stop":
                print("Zatrzymano.")
                exit()
            elif text !="":
                print("Koniec czasu.")
                print("nie rozpoznano, powiedziano")
                return text
                print("?")
            else:
                print("Koniec czasu.")
                print("niepoprawne")                    
                return 0            
        except:
            return 0
    txt = textparser()
    if not txt == 0:
        print('Zrozumialem')
        print(txt)
        mow(txt)
        textparser()
    else:
        print("Koniec czasu.")
        print('nie udalo sie rozpoznac mowy')
        textparser()

textparser()
