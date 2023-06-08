import sys, os, winsound, PIL.Image, random, webbrowser, time
import speech_recognition as sr
import pyttsx3 as tts

r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


wybor_zaaw = ''
termin = [['', '']]
poziom_zaaw = []
lista_uzyt = []
lista_pliki = []
global dzien
dzien = ''
global godzina
godzina = ''
global imie
imie = ''
global nazwisko
nazwisko = ''

clear = lambda: os.system('cls')


def start():
    # print('Ladowanie programu, prosze czekac.')
    # for x in range (0,3):
    # b = "." * x
    # print (b, end="\r")
    # time.sleep(1)
    print('\n' + 'Witaj! Dodzwoniles sie do najlepszej plywalni w miescie.' + '\n')
    # winsound.PlaySound('WAV/basen.wav', winsound.SND_ASYNC)
    intro()


def intro():
    print('\n' + 'Aby sprawdzic dostepnosc torow wybierz 1.\nAby umowic sie na zejcia z instruktorem wybierz 2.\nAby zarezerwowac tor wybierz 3.\nAby otworzyc grafik wybierz 4.\nAby otworzyc strone internetowa basenu wybierz 5.\nAby otworzyc panel administratora wybierz 6.' + '\n')
    print('Co chcesz zrobic(1,2,3,4,5,6)?' + '\n' + 'Numer:')
    print('Slucham...')
    intro_1()


def intro_1():
    wybor = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
            # mow(wybor_audio)
        except:
            print(end='.')
            intro_1()
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
            intro_1()
        print('\n' + 'Wybrales numer: ' + wybor + '\n')
        if wybor == str(1):
            print('\n' + 'Chcesz sprawdzic dostepnosc torow.')
            print('dobrze')
            wybor1DzienPrinty()
        if wybor == str(2):
            print('\n' + 'Chcesz zamowic zajecia z instruktorem.')
            wybor2Printy()
        if wybor == str(3):
            print('\n' + 'Chcesz zarezerowac tor.')
            wybor3Printy()
        if wybor == str(4):
            print('\n' + 'Chcesz otworzyc grafik.')
            grafik()
        if wybor == str(5):
            print('\n' + 'Chcesz otworzyc strone internetowa basenu.')
            stronainternetowa()
        if wybor == str(6):
            print('\n' + 'Otwieranie panelu administratora.')
            hasloadmina()
        else:
            print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
            intro()


def wybor1DzienPrinty():
    clear()
    print('\n' + 'Na jaki dzien sprawdzic dostepnosc?')
    print('\n' + 'Podaj dzień: ' + '\n')
    print('Słucham...')
    wybor1Dzien()


def wybor1Dzien():
    global dzien
    dzien = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor1Dzien()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            dzien = str(1)
        elif wybor_audio == '1':
            dzien = str(1)
        elif wybor_audio == '2':
            dzien = str(2)
        elif wybor_audio == '3':
            dzien = str(3)
        elif wybor_audio == '4':
            dzien = str(4)
        elif wybor_audio == 'pięć':
            dzien = str(5)
        elif wybor_audio == '5':
            dzien = str(5)
        elif wybor_audio == '6':
            dzien = str(6)
        elif wybor_audio == '7':
            dzien = str(7)
        elif wybor_audio == 'siedem':
            dzien = str(7)
        elif wybor_audio == 'poniedziałek':
            dzien = str(1)
        elif wybor_audio == 'wtorek':
            dzien = str(2)
        elif wybor_audio == 'środa':
            dzien = str(3)
        elif wybor_audio == 'czwartek':
            dzien = str(4)
        elif wybor_audio == 'piątek':
            dzien = str(5)
        elif wybor_audio == 'sobota':
            dzien = str(6)
        elif wybor_audio == 'niedziela':
            dzien = str(7)
        else:
            wybor1Dzien()
    print(dzien)
    wybor1GodzinaPrinty()


def wybor1GodzinaPrinty():
    print('\n' + 'Podaj godzine (tylko pelne godziny od 6 do 20 godziny): ' + '\n')
    print('Słucham...')
    wybor1Godzina()


def wybor1Godzina():
    global godzina
    godzina = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor1Godzina()
        print(wybor_audio)
        if wybor_audio == 'szósta':
            godzina = str(6)
        elif wybor_audio == 'siódma':
            godzina = str(7)
        elif wybor_audio == 'ósma':
            godzina = str(8)
        elif wybor_audio == 'dziewiąta':
            godzina = str(9)
        elif wybor_audio == 'dziesiąta':
            godzina = str(10)
        elif wybor_audio == 'jedenasta':
            godzina = str(11)
        elif wybor_audio == 'dwunasta':
            godzina = str(12)
        elif wybor_audio == 'trzynasta':
            godzina = str(13)
        elif wybor_audio == 'czternasta':
            godzina = str(14)
        elif wybor_audio == 'piętnasta':
            godzina = str(15)
        elif wybor_audio == 'szesnasta':
            godzina = str(16)
        elif wybor_audio == 'siedemnasta':
            godzina = str(17)
        elif wybor_audio == 'osiemnasta':
            godzina = str(18)
        elif wybor_audio == 'dziewiętnasta':
            godzina = str(19)
        elif wybor_audio == 'dwudziesta':
            godzina = str(20)
        if wybor_audio == '6:00':
            godzina = str(6)
        elif wybor_audio == '7:00':
            godzina = str(7)
        elif wybor_audio == '8:00':
            godzina = str(8)
        elif wybor_audio == '9:00':
            godzina = str(9)
        elif wybor_audio == '10:00':
            godzina = str(10)
        elif wybor_audio == '11:00':
            godzina = str(11)
        elif wybor_audio == '12:00':
            godzina = str(12)
        elif wybor_audio == '13:00':
            godzina = str(13)
        elif wybor_audio == '14:00':
            godzina = str(14)
        elif wybor_audio == '15:00':
            godzina = str(15)
        elif wybor_audio == '16:00':
            godzina = str(16)
        elif wybor_audio == '17:00':
            godzina = str(17)
        elif wybor_audio == '18:00':
            godzina = str(18)
        elif wybor_audio == '19:00':
            godzina = str(19)
        elif wybor_audio == '20:00':
            godzina = str(20)
        else:
            wybor1Godzina()
    #print(dzien)
    #print(godzina)
    wybor1()


def wybor1():
    zajety = 0
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin:
                    if element[0] == dzien:
                        if element[1] == godzina:
                            print('\n' + 'Tor w tym terminie jest zajety.' + '\n\n')
                            zajety = 1
                            intro()
                if zajety == 0:
                    print('\n' + 'Tory o tej godzine sa dostepne.' + '\n')
                    print('\n' + 'Aby zarezerwowac tor wybierz 1' + '\n' + 'Aby zamowic zajecia z instruktorem wybierz 2' + '\n' + 'Aby wrocic do menu glownego wybierz 3.' + '\n')
                    print('Słucham...')
                    wybor1_2()
            else:
                print('\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                wybor1_3()
    else:
        print('Potrzebna liczba!' + '\n')
        wybor1DzienPrinty()


def wybor1_2():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor1_2()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            wybor_inna_opcja = str(1)
        elif wybor_audio == '1':
            wybor_inna_opcja = str(1)
        elif wybor_audio == '2':
            wybor_inna_opcja = str(2)
        elif wybor_audio == '3':
            wybor_inna_opcja = str(3)
        else:
            wybor1_2()
    if wybor_inna_opcja == str(1):
        wybor3()
    if wybor_inna_opcja == str(2):
        wybor2()
    if wybor_inna_opcja == str(3):
        intro()


def wybor1_3():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor1_3()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            wybor_inna_opcja = str(1)
        elif wybor_audio == '1':
            wybor_inna_opcja = str(1)
        elif wybor_audio == '2':
            wybor_inna_opcja = str(2)
        else:
            wybor1_3()
    if wybor_inny_termin == str(1):
        wybor1()
    if wybor_inny_termin == str(2):
        intro()


def wybor2Printy():
    print('\n' + 'Wybierz poziom zaawansowania:' + '\n' + 'Poczatkujacy(1)' + '\n' + 'Sredniozaawansowany(2)' + '\n' + 'Zaawansowany(3)' + '\n')
    print('Słucham...')
    wybor2()


def wybor2():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor2()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            wybor_zaaw = str(1)
        elif wybor_audio == '1':
            wybor_zaaw = str(1)
        elif wybor_audio == '2':
            wybor_zaaw = str(2)
        elif wybor_audio == '3':
            wybor_zaaw = str(3)
        else:
            wybor2()
    if wybor_zaaw == str(1):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom poczatkujacy')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3Printy()
    if wybor_zaaw == str(2):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom sredniozaawansowany')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3Printy()
    if wybor_zaaw == str(3):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom zaawansowany')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3Printy()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        wybor2Printy()


def wybor3Printy():
    print('Wybrano rezerwacje toru.')
    wybor3DzienPrinty()


def wybor3DzienPrinty():
    print('\n' + 'Na jaki dzien zarezerwowac tor?')
    print('\n' + 'Podaj numer dnia(gdzie poniedzialek = 1, niedziela = 7): ' + '\n')
    wybor3Dzien()


def wybor3Dzien():
    global dzien
    dzien = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3Dzien()
        print(wybor_audio)
        if wybor_audio == 'jeden':
            dzien = str(1)
        elif wybor_audio == '1':
            dzien = str(1)
        elif wybor_audio == '2':
            dzien = str(2)
        elif wybor_audio == '3':
            dzien = str(3)
        elif wybor_audio == '4':
            dzien = str(4)
        elif wybor_audio == 'pięć':
            dzien = str(5)
        elif wybor_audio == '5':
            dzien = str(5)
        elif wybor_audio == '6':
            dzien = str(6)
        elif wybor_audio == '7':
            dzien = str(7)
        elif wybor_audio == 'siedem':
            dzien = str(7)
        elif wybor_audio == 'poniedziałek':
            dzien = str(1)
        elif wybor_audio == 'wtorek':
            dzien = str(2)
        elif wybor_audio == 'środa':
            dzien = str(3)
        elif wybor_audio == 'czwartek':
            dzien = str(4)
        elif wybor_audio == 'piątek':
            dzien = str(5)
        elif wybor_audio == 'sobota':
            dzien = str(6)
        elif wybor_audio == 'niedziela':
            dzien = str(7)
        else:
            wybor3Dzien()
    print(dzien)
    wybor3GodzinaPrinty()


def wybor3GodzinaPrinty():
    print('\n' + 'Podaj godzine (tylko pelne godziny do 6 do 20 godziny): ' + '\n')
    wybor3Godzina()


def wybor3Godzina():
    global godzina
    godzina = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3Godzina()
        print(wybor_audio)
        if wybor_audio == 'szósta':
            godzina = str(6)
        elif wybor_audio == 'siódma':
            godzina = str(7)
        elif wybor_audio == 'ósma':
            godzina = str(8)
        elif wybor_audio == 'dziewiąta':
            godzina = str(9)
        elif wybor_audio == 'dziesiąta':
            godzina = str(10)
        elif wybor_audio == 'jedenasta':
            godzina = str(11)
        elif wybor_audio == 'dwunasta':
            godzina = str(12)
        elif wybor_audio == 'trzynasta':
            godzina = str(13)
        elif wybor_audio == 'czternasta':
            godzina = str(14)
        elif wybor_audio == 'piętnasta':
            godzina = str(15)
        elif wybor_audio == 'szesnasta':
            godzina = str(16)
        elif wybor_audio == 'siedemnasta':
            godzina = str(17)
        elif wybor_audio == 'osiemnasta':
            godzina = str(18)
        elif wybor_audio == 'dziewiętnasta':
            godzina = str(19)
        elif wybor_audio == 'dwudziesta':
            godzina = str(20)
        if wybor_audio == '6:00':
            godzina = str(6)
        elif wybor_audio == '7:00':
            godzina = str(7)
        elif wybor_audio == '8:00':
            godzina = str(8)
        elif wybor_audio == '9:00':
            godzina = str(9)
        elif wybor_audio == '10:00':
            godzina = str(10)
        elif wybor_audio == '11:00':
            godzina = str(11)
        elif wybor_audio == '12:00':
            godzina = str(12)
        elif wybor_audio == '13:00':
            godzina = str(13)
        elif wybor_audio == '14:00':
            godzina = str(14)
        elif wybor_audio == '15:00':
            godzina = str(15)
        elif wybor_audio == '16:00':
            godzina = str(16)
        elif wybor_audio == '17:00':
            godzina = str(17)
        elif wybor_audio == '18:00':
            godzina = str(18)
        elif wybor_audio == '19:00':
            godzina = str(19)
        elif wybor_audio == '20:00':
            godzina = str(20)
        else:
            wybor3Godzina()
    #print(dzien)
    #print(godzina)
    wybor3()


def wybor3():
    lista_uzyt = []
    imie = ''
    nazwisko = ''
    imie = input('Aby rozpoczac rezerwacje, wpisz najpierw swoje imie i wcisnij enter' + '\n')
    nazwisko = input('I teraz wpisz nazwisko i wcisnij enter:' + '\n')
    zajety = 0
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin or truetermin:
                    if element[0] == str(dzien):
                        if element[1] == str(godzina):
                            zajety = 1
                            print('\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                            wybor3_1()
                if zajety == 0:
                    lista_uzyt.append(dzien)
                    # print(lista_uzyt)
                    lista_uzyt.append(godzina)
                    # print(lista_uzyt)
                    termin.append(lista_uzyt)
                    # print(termin)
                    outfile = open('dane.txt', 'a')
                    outfile.write(
                        dzien + '\t' + godzina + '\t' + imie + '\t' + nazwisko + '\t' + str(poziom_zaaw) + '\n')
                    outfile.close()
                    # print(str(poziom_zaaw))
                    print('\n' + 'Dziekujemy za skorzystanie z uslugi uzytkowniku' + ' ' + imie + ' ' + nazwisko + '!')
                    print('\n' + 'Wybrano nastepujace dni i godziny [i poziom zaawansowania]:')
                    if dzien == str(1):
                        print('Poniedzialek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(2):
                        print('Wtorek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(3):
                        print('Sroda godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(4):
                        print('Czwartek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(5):
                        print('Piatek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(6):
                        print('Sobota godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(7):
                        print('Niedziela godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    list.clear(poziom_zaaw)
                    dzieki()
            else:
                print(
                    '\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                wybor3_2()
    else:
        print('Potrzebna liczba!' + '\n')
        wybor3()


def wybor3_1():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3_1()
        if wybor_audio == 'jeden':
            zmiana = str(1)
        elif wybor_audio == '1':
            zmiana = str(1)
        elif wybor_audio == '2':
            zmiana = str(2)
        else:
            wybor3_1()
    if zmiana == str(1):
        wybor3Printy()
    if zmiana == str(2):
        intro()


def wybor3_2():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3_2()
        if wybor_audio == 'jeden':
            zmiana_2 = str(1)
        elif wybor_audio == '1':
            zmiana_2 = str(1)
        elif wybor_audio == '2':
            zmiana_2 = str(2)
        else:
            wybor3()
    if zmiana_2 == str(1):
        wybor3Printy()
    if zmiana_2 == str(2):
        intro()


def stronainternetowa():
    webbrowser.open('https://posir.poznan.pl/obiekty/winogrady/plywalnia-kryta', new=0, autoraise=True)
    intro()


def grafik():
    grafikzdjecie = PIL.Image.open('JPG/grafik.jpg')
    grafikzdjecie.show()
    print('Wyswietlono grafik.')
    intro()


def dziekiPrinty():
    print('\nAby wrocic do menu glownego wybierz 1.\nAby wyswietlic motywujaca wiadmosc wybierz 2.' + '\n')
    print('Co chcesz zrobic(1,2)?' + '\n' + 'Numer:')
    dzieki()


def dzieki():
    zmiana_3 = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3_2()
        if wybor_audio == 'jeden':
            zmiana_3 = str(1)
        elif wybor_audio == '1':
            zmiana_3 = str(1)
        elif wybor_audio == '2':
            zmiana_3 = str(2)
        else:
            wybor3()
    if zmiana_3 == str(1):
        print('\n' + 'Wybrales numer: ' + zmiana_3 + '\n')
        print('\n' + 'Wybrano powrot do menu.')
        # print('Ladowanie programu, prosze czekac.')
        # for x in range (0,3):
        # b = "." * x
        # print (b, end="\r")
        # time.sleep(1)
        intro()
    if zmiana_3 == str(2):
        print('\n' + 'Wybrales numer: ' + zmiana_3 + '\n')
        plik = open('TEXT/motywacja.txt')
        motywacja = plik.readlines()
        plik.close()
        losowe = random.choice(motywacja)
        dawaj = losowe.strip()
        print(dawaj)
        dziekiPrinty()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        dziekiPrinty()


def hasloadmina():
    haslo = 'tosty7'
    print('Prosze czekac.')
    for x in range(0, 3):
        b = "." * x
        print(b, end="\r")
        time.sleep(1)
    print('\n' + 'Podaj haslo:' + '\n')
    podanehaslo = input()
    if podanehaslo == haslo:
        print('Sprawdzanie hasla.')
        for x in range(0, 3):
            b = "." * x
            print(b, end="\r")
            time.sleep(1)
        paneladministratora()
    else:
        print('Niepoprawne haslo!')
        intro()


def paneladministratora():
    print('\n' + 'Witaj administratorze.')
    print('Aby wyswietlic tabele wybierz 1.\nAby wyczycic wszystkie tabele wybierz 2.\nAby zakonczyc program wybierz 3.\nAby wrocic do menu glownego 4.\n')
    wyboradmin = ''
    wyboradmin = input('Co chcesz zrobic(1,2,3)?' + '\n' + 'Numer:')
    if wyboradmin == str(1):
        print('\n' + 'Oto tabele:' + '\n')
        print(termin)
        paneladministratora()
    if wyboradmin == str(2):
        print('\n' + 'Rozpoczynam czyszczenie tabel.' + '\n')
        time.sleep(1)
        czyszczenietabel()
    if wyboradmin == str(3):
        print('\n' + 'Koncze program.' + '\n')
        time.sleep(1)
        end()
    if wyboradmin == str(4):
        print('\n' + 'Wracam do menu.' + '\n')
        time.sleep(1)
        intro()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        paneladministratora()


def czyszczenietabel():
    list.clear(termin)
    termindodaj = ['', '']
    termin.append(termindodaj)
    print('Tabele wyczyszczone!')
    paneladministratora()


def end():
    exit()

start()
