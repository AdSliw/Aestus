import winsound, PIL.Image, random, webbrowser, time
from datetime import datetime
import speech_recognition as sr
import pyttsx3 as tts
import cowsay

#TODO Przygotować ankietę!


p_reco = 0
if p_reco == 1:
    r = sr.Recognizer()
if p_reco == 0:
    pass
engine = tts.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
p_mowy = 0


def mow(text):
    global p_mowy
    if p_mowy == 1:
        engine.say(text)
        engine.runAndWait()
    if p_mowy == 0:
        pass


termin = [['', '']]
termin_usunieto = []
termin_pracy = [[['  '], [' ', ' '], [' ', '  ']]]
termin_pracy_pomocniczy = []
numer_pracownika = []
lista_pomocnicza_godzin = []
lista_pomocnicza_dni = []
lista_pomocnicza_numeru_pracownika = []
termin_usunieto_pracowniczy = []
termin_usunieto_uzytkownika = []
wybor_zaaw = ''
poziom_zaaw = []
lista_uzyt = []
lista_pliki = []
#global dzien
dzien = ''
#global godzina
godzina = ''
#global imie
imie = ''
#global nazwisko
nazwisko = ''


teraz = datetime.now()
outfile1 = open('usuniete_tabele.txt', 'a')
outfile1.write('\n' + 'Nowa instancja programu. Sygnatura instancji: ' + str(teraz) + '\n' +
               '- - - - - - - - - - - - - - - - - - - - - - - - - -' + '\n')
outfile1.write('Czas wykonania operacji:' + '\t' + 'ID' + ':' + '\t' + '[D: , G: ]' + '\t' + '\n')
outfile1.close()

outfile2 = open('usuniete_terminy_pracownicze.txt', 'a')
outfile2.write('\n' + 'Nowa instancja programu. Sygnatura instancji: ' + str(teraz) + '\n' +
               '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -' + '\n')
outfile2.write('Czas wykonania operacji:' + '\t' + 'ID' + ':' + '\t' + '[[Nr: ], [M: , D: ], [S: , K: ]]' + '\t' + '\n')
outfile2.close()

mowa_menu_bool = False
instrukcja_bool = False

def start():
    winsound.PlaySound('WAV/basen.wav', winsound.SND_ASYNC)
    print('Witaj w programie Aestus.' + '\n'
          '                    _             ' + '\n'                              
          '     /\            | |            ' + '\n'
          '    /  \   ___  ___| |_ _   _ ___ ' + '\n'
          '   / /\ \ / _ \/ __| __| | | / __|' + '\n'
          '  / ____ \  __/\__ \ |_| |_| \__ \ ' + '\n'
          ' /_/    \_\___||___/\__|\__,_|___/ v1.3' + '\n')
    print('Ładowanie...')
    time.sleep(3)
    mow('Witaj w programie Estós!') #tts generuje ó i u inaczej
    intro()


#todo instrukcja


def instrukcja():
    print('Oto krótka instrukcja.'
          '\n\nAby wybierać poszczególne opcje z menu '
          '\nużywaj głosowych zwrotów: jeden, dwa, trzy, itd.'
          '\nPrzy wyborze dnia i godziny, używaj głosowych zwrotów: '
          '\nponiedziałek, środa, niedziela, szósta, dwunatsta, dziewiętnasta itd.'
          '\nPrzy wpisywaniu Imienia i Nazwiska jak i wybieraniu opcji'
          '\nw panelu pracownika i administratora używaj klawiatury. '
          '\nAby wyświetlić instrukcję ponownie, wybierz opcję 0.'
          '\n\n')
    mow('Oto krótka instrukcja. '
        'Aby wybierać poszczególne opcje z menu '
        'używaj głosowych zwrotów: jeden, dwa, trzy, i tak dalej. '
        'Przy wyborze dnia i godziny, używaj głosowych zwrotów: '
        'poniedziałek, środa, niedziela, szósta, dwunatsta, dziewiętnasta i tak dalej. '
        'Przy wpisywaniu Imienia i Nazwiska jak i wybieraniu opcji'
        ' w panelu pracownika i administratora używaj klawiatury. '
        'Aby wyświetlić instrukcję ponownie wybierz opcje zero.')


def intro():
    global instrukcja_bool
    global mowa_menu_bool
    print('\n' + 'Powiedz: ' + '\n' +
                 '1 - Aby sprawdzić dostępność torów.'
                 '\n2 - Aby zamówić zajęcia z instruktorem.'
                 '\n3 - Aby zarezerwować tor.'
                 '\n4 - Aby otworzyć grafik.'
                 '\n5 - Aby otworzyć stronę internetową basenu.'
                 '\n6 - Aby otworzyć panel pracowniczy.'
                 '\n7 - Aby otworzyć panel administratora.'
                 '\n0 - Aby wyświetlić instrukcję.' + '\n')
    if mowa_menu_bool:
        mow('Powiec: ' 
            '1 - Aby sprawdzić dostępność torów. '
            '2 - Aby zamówić zajęcia z instruktorem. '
            '3 - Aby zarezerwować tor. '
            '4 - Aby otworzyć grafik. '
            '5 - Aby otworzyć stronę internetową basenu.')
        mowa_menu_bool = False
            # '6 - Aby otworzyć panel pracowniczy.'
            # '7 - Aby otworzyć panel administratora.')
    if instrukcja_bool:
        instrukcja()
        instrukcja_bool = False

    print('Co chcesz zrobić?' + '\n' + 'Numer:')
    mow('Co chcesz zrobić?')
    print('Słucham...')
    mow('Słucham')
    intro_1()


def intro_1():
    wybor = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                if wybor_audio == 'jeden':
                    wybor = str(1)
                elif wybor_audio == '1':
                    wybor = str(1)
                elif wybor_audio == '2':
                    wybor = str(2)
                elif wybor_audio == 'czy':
                    wybor = str(3)
                elif wybor_audio == '3':
                    wybor = str(3)
                elif wybor_audio == '4':
                    wybor = str(4)
                elif wybor_audio == 'pięć':
                    wybor = str(5)
                elif wybor_audio == '5':
                    wybor = str(5)
                elif wybor_audio == 'cześć':
                    wybor = str(6)
                elif wybor_audio == '6':
                    wybor = str(6)
                elif wybor_audio == '7':
                    wybor = str(7)
                elif wybor_audio == 'siedem':
                    wybor = str(7)
                elif wybor_audio == 'zero':
                    wybor = str(0)
                elif wybor_audio == '0':
                    wybor = str(0)
                else:
                    intro_1()
                print('\n' + 'Wybrano numer: ' + wybor)
                mow('Wybrano numer: ' + wybor)
                if wybor == str(1):
                    print('\n' + 'Chcesz sprawdzić dostępność torów.')
                    mow('Chcesz sprawdzić dostępność torów.')
                    wybor1DzienPrinty()
                if wybor == str(2):
                    print('\n' + 'Chcesz zamówić zajęcia z instruktorem.')
                    mow('Chcesz zamowić zajęcia z instruktorem.')
                    wybor2Printy()
                if wybor == str(3):
                    print('\n' + 'Chcesz zarezerować tor.')
                    mow('Chcesz zarezerwować tor.')
                    wybor3Printy()
                if wybor == str(4):
                    print('\n' + 'Chcesz otworzyć grafik.')
                    mow('Chcesz otworzyć grafik.')
                    grafik()
                if wybor == str(5):
                    print('\n' + 'Chcesz otworzyć stronę internetową basenu.')
                    mow('Chcesz otworzyć stronę internetową basenu.')
                    stronainternetowa()
                if wybor == str(6):
                    print('\n' + 'Otwieranie panelu pracowniczego.')
                    mow('Otwieranie panelu pracowniczego.')
                    haslop()
                if wybor == str(7):
                    print('\n' + 'Otwieranie panelu administratora.')
                    mow('Otwieranie panelu administratora.')
                    hasloa()
                if wybor == str(0):
                    print('\n' + 'Otwieranie instrukcji.')
                    mow('Otwieranie instrukcji.')
                    instrukcja()
                    intro()
                else:
                    print('\n' + 'Proszę wybrać odpowiednią liczbę!1' + '\n' + '\n')
                    mow('Proszę wybrać odpowiednią liczbę.')
                    intro()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            print('Słucham...')
            mow('Słucham')
            intro_1()
        elif wybor_awaryjny_input == str('2'):
            wybor_a = ''
            wybor_audio_a = input('Którą opcję wybierasz?\n')
            if wybor_audio_a == 'jeden':
                wybor_a = str(1)
            elif wybor_audio_a == '1':
                wybor_a = str(1)
            elif wybor_audio_a == '2':
                wybor_a = str(2)
            elif wybor_audio_a == 'czy':
                wybor_a = str(3)
            elif wybor_audio_a == '3':
                wybor_a = str(3)
            elif wybor_audio_a == '4':
                wybor_a = str(4)
            elif wybor_audio_a == 'pięć':
                wybor_a = str(5)
            elif wybor_audio_a == '5':
                wybor_a = str(5)
            elif wybor_audio_a == 'cześć':
                wybor_a = str(6)
            elif wybor_audio_a == '6':
                wybor_a = str(6)
            elif wybor_audio_a == '7':
                wybor_a = str(7)
            elif wybor_audio_a == 'siedem':
                wybor_a = str(7)
            elif wybor_audio_a == 'zero':
                wybor_a = str(0)
            elif wybor_audio_a == '0':
                wybor_a = str(0)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            print('\n' + 'Wybrano numer: ' + wybor_a)
            mow('Wybrano numer: ' + wybor_a)
            if wybor_a == str(1):
                print('\n' + 'Chcesz sprawdzić dostępność torów.')
                mow('Chcesz sprawdzić dostępność torów.')
                wybor1DzienPrinty()
            if wybor_a == str(2):
                print('\n' + 'Chcesz zamówić zajęcia z instruktorem.')
                mow('Chcesz zamowić zajęcia z instruktorem.')
                wybor2Printy()
            if wybor_a == str(3):
                print('\n' + 'Chcesz zarezerować tor.')
                mow('Chcesz zarezerwować tor.')
                wybor3Printy()
            if wybor_a == str(4):
                print('\n' + 'Chcesz otworzyć grafik.')
                mow('Chcesz otworzyć grafik.')
                grafik()
            if wybor_a == str(5):
                print('\n' + 'Chcesz otworzyć stronę internetową basenu.')
                mow('Chcesz otworzyć stronę internetową basenu.')
                stronainternetowa()
            if wybor_a == str(6):
                print('\n' + 'Otwieranie panelu pracowniczego.')
                mow('Otwieranie panelu pracowniczego.')
                haslop()
            if wybor_a == str(7):
                print('\n' + 'Otwieranie panelu administratora.')
                mow('Otwieranie panelu administratora.')
                hasloa()
            if wybor_a == str(0):
                print('\n' + 'Otwieranie instrukcji.')
                mow('Otwieranie instrukcji.')
                instrukcja()
                intro()
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                intro()
        else:
            print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
            mow('Proszę wybrać odpowiednią liczbę.')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor1DzienPrinty():
    print('\n' + 'Na jaki dzień sprawdzić dostępność?')
    mow('Na jaki dzień sprawdzić dostępność')
    print('\n' + 'Podaj dzień: ')
    mow('Podaj dzień')
    print('Słucham...')
    mow('Słucham')
    wybor1Dzien()


def wybor1Dzien():
    global dzien
    dzien = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
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
                elif wybor_audio == 'pierwszy':
                    dzien = str(1)
                elif wybor_audio == 'drugi':
                    dzien = str(2)
                elif wybor_audio == 'trzeci':
                    dzien = str(3)
                elif wybor_audio == 'czwarty':
                    dzien = str(4)
                elif wybor_audio == 'piąty':
                    dzien = str(5)
                elif wybor_audio == 'szósty':
                    dzien = str(6)
                elif wybor_audio == 'siódmy':
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
                elif wybor_audio == 'Poniedziałek':
                    dzien = str(1)
                elif wybor_audio == 'Wtorek':
                    dzien = str(2)
                elif wybor_audio == 'Środa':
                    dzien = str(3)
                elif wybor_audio == 'Czwartek':
                    dzien = str(4)
                elif wybor_audio == 'Piątek':
                    dzien = str(5)
                elif wybor_audio == 'Sobota':
                    dzien = str(6)
                elif wybor_audio == 'Niedziela':
                    dzien = str(7)
                else:
                    wybor1Dzien()
                # print(dzien)
                if dzien == str(1):
                    print('Wybrano poniedziałek.')
                    mow('Wybrano poniedziałek.')
                elif dzien == str(2):
                    print('Wybrano wtorek.')
                    mow('Wybrano wtorek.')
                elif dzien == str(3):
                    print('Wybrano środę.')
                    mow('Wybrano środę.')
                elif dzien == str(4):
                    print('Wybrano czwartek.')
                    mow('Wybrano czwartek.')
                elif dzien == str(5):
                    print('Wybrano piątek')
                    mow('Wybrano piątek')
                elif dzien == str(6):
                    print('Wybrano sobotę.')
                    mow('Wybrano sobotę.')
                elif dzien == str(7):
                    print('Wybrano niedzielę.')
                    mow('Wybrano niedzielę.')
                else:
                    wybor1Dzien()
                wybor1GodzinaPrinty()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor1Dzien()
        elif wybor_awaryjny_input == str('2'):
            global dzien
            dzien = ''
            wybor_audio = input('Który dzień wybierasz?\n')
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
            elif wybor_audio == 'pierwszy':
                dzien = str(1)
            elif wybor_audio == 'drugi':
                dzien = str(2)
            elif wybor_audio == 'trzeci':
                dzien = str(3)
            elif wybor_audio == 'czwarty':
                dzien = str(4)
            elif wybor_audio == 'piąty':
                dzien = str(5)
            elif wybor_audio == 'szósty':
                dzien = str(6)
            elif wybor_audio == 'siódmy':
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
            elif wybor_audio == 'Poniedziałek':
                dzien = str(1)
            elif wybor_audio == 'Wtorek':
                dzien = str(2)
            elif wybor_audio == 'Środa':
                dzien = str(3)
            elif wybor_audio == 'Czwartek':
                dzien = str(4)
            elif wybor_audio == 'Piątek':
                dzien = str(5)
            elif wybor_audio == 'Sobota':
                dzien = str(6)
            elif wybor_audio == 'Niedziela':
                dzien = str(7)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            # print(dzien)
            if dzien == str(1):
                print('Wybrano poniedziałek.')
                mow('Wybrano poniedziałek.')
            elif dzien == str(2):
                print('Wybrano wtorek.')
                mow('Wybrano wtorek.')
            elif dzien == str(3):
                print('Wybrano środę.')
                mow('Wybrano środę.')
            elif dzien == str(4):
                print('Wybrano czwartek.')
                mow('Wybrano czwartek.')
            elif dzien == str(5):
                print('Wybrano piątek')
                mow('Wybrano piątek')
            elif dzien == str(6):
                print('Wybrano sobotę.')
                mow('Wybrano sobotę.')
            elif dzien == str(7):
                print('Wybrano niedzielę.')
                mow('Wybrano niedzielę.')
            else:
                wybor1Dzien()
            wybor1GodzinaPrinty()
        else:
            print('Proszę wybrać odpowiednią opcję. ')
            mow('Proszę wybrać odpowiednią opcję. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor1GodzinaPrinty():
    print('\n' + 'Podaj godzinę (tylko pelne godziny od 6 do 20 godziny): ' + '\n')
    mow('Podaj godzinę, obowiązują tylko pełne godziny od szóstej do dwudziestej. ')
    print('Słucham...')
    mow('Słucham')
    wybor1Godzina()


def wybor1Godzina():
    global godzina
    godzina = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
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
                elif wybor_audio == 'pietnasta':
                    godzina = str(15)
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
                elif wybor_audio == '6':
                    godzina = str(6)
                elif wybor_audio == '7':
                    godzina = str(7)
                elif wybor_audio == '8':
                    godzina = str(8)
                elif wybor_audio == '9':
                    godzina = str(9)
                elif wybor_audio == '10':
                    godzina = str(10)
                elif wybor_audio == '11':
                    godzina = str(11)
                elif wybor_audio == '12':
                    godzina = str(12)
                elif wybor_audio == '13':
                    godzina = str(13)
                elif wybor_audio == '14':
                    godzina = str(14)
                elif wybor_audio == '15':
                    godzina = str(15)
                elif wybor_audio == '16':
                    godzina = str(16)
                elif wybor_audio == '17':
                    godzina = str(17)
                elif wybor_audio == '18':
                    godzina = str(18)
                elif wybor_audio == '19':
                    godzina = str(19)
                elif wybor_audio == '20':
                    godzina = str(20)
                elif wybor_audio == 'sześć':
                    godzina = str(6)
                elif wybor_audio == 'siedem':
                    godzina = str(7)
                elif wybor_audio == 'osiem':
                    godzina = str(8)
                elif wybor_audio == 'dziewięć':
                    godzina = str(9)
                elif wybor_audio == 'dziesięć':
                    godzina = str(10)
                elif wybor_audio == 'jedenaście':
                    godzina = str(11)
                elif wybor_audio == 'dwanaście':
                    godzina = str(12)
                elif wybor_audio == 'trzynaście':
                    godzina = str(13)
                elif wybor_audio == 'czternaście':
                    godzina = str(14)
                elif wybor_audio == 'piętnaście':
                    godzina = str(15)
                elif wybor_audio == 'szesnaście':
                    godzina = str(16)
                elif wybor_audio == 'siedemnaście':
                    godzina = str(17)
                elif wybor_audio == 'osiemnaście':
                    godzina = str(18)
                elif wybor_audio == 'dziewiętnaście':
                    godzina = str(19)
                elif wybor_audio == 'dwadzieścia':
                    godzina = str(20)
                else:
                    wybor1Godzina()
                if godzina == str(6):
                    print('Wybrano godzinę 6:00')
                    mow('Wybrano godzinę szóstą')
                elif godzina == str(7):
                    print('Wybrano godzinę 7:00.')
                    mow('Wybrano godzinę siódmą.')
                elif godzina == str(8):
                    print('Wybrano godzinę 8:00.')
                    mow('Wybrano godzinę ósmą.')
                elif godzina == str(9):
                    print('Wybrano godzinę 9:00.')
                    mow('Wybrano godzinę dziewiątą.')
                elif godzina == str(10):
                    print('Wybrano godzinę 10:00.')
                    mow('Wybrano godzinę dziesiątą.')
                elif godzina == str(11):
                    print('Wybrano godzinę 11:00.')
                    mow('Wybrano godziną jedenastą.')
                elif godzina == str(12):
                    print('Wybrano godzinę 12:00.')
                    mow('Wybrano godzinę dwunastą.')
                elif godzina == str(13):
                    print('Wybrano godzinę 13:00.')
                    mow('Wybrano godzinę trzynastą.')
                elif godzina == str(14):
                    print('Wybrano godzinę 14:00.')
                    mow('Wybrano godzinę czternastą.')
                elif godzina == str(15):
                    print('Wybrano godzinę 15:00.')
                    mow('Wybrano godzinę piętnastą.')
                elif godzina == str(16):
                    print('Wybrano godzinę 16:00.')
                    mow('Wybrano godzinę szesnastą.')
                elif godzina == str(17):
                    print('Wybrano godzinę 17:00.')
                    mow('Wybrano godzinę siedemnastą.')
                elif godzina == str(18):
                    print('Wybrano godzinę 18:00.')
                    mow('Wybrano godzinę osiemnastą.')
                elif godzina == str(19):
                    print('Wybrano godzinę 19:00.')
                    mow('Wybrano godzinę dziewiętnastą.')
                elif godzina == str(20):
                    print('Wybrano godzinę 20:00.')
                    mow('Wybrano godzinę dwudziestą.')
                else:
                    wybor1Godzina()
                wybor1()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor1Godzina()
        elif wybor_awaryjny_input == str('2'):
            global godzina
            godzina = ''
            wybor_audio = input('Którą godzinę wybierasz?\n')
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
            elif wybor_audio == 'pietnasta':
                godzina = str(15)
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
            elif wybor_audio == '6':
                godzina = str(6)
            elif wybor_audio == '7':
                godzina = str(7)
            elif wybor_audio == '8':
                godzina = str(8)
            elif wybor_audio == '9':
                godzina = str(9)
            elif wybor_audio == '10':
                godzina = str(10)
            elif wybor_audio == '11':
                godzina = str(11)
            elif wybor_audio == '12':
                godzina = str(12)
            elif wybor_audio == '13':
                godzina = str(13)
            elif wybor_audio == '14':
                godzina = str(14)
            elif wybor_audio == '15':
                godzina = str(15)
            elif wybor_audio == '16':
                godzina = str(16)
            elif wybor_audio == '17':
                godzina = str(17)
            elif wybor_audio == '18':
                godzina = str(18)
            elif wybor_audio == '19':
                godzina = str(19)
            elif wybor_audio == '20':
                godzina = str(20)
            elif wybor_audio == 'sześć':
                godzina = str(6)
            elif wybor_audio == 'siedem':
                godzina = str(7)
            elif wybor_audio == 'osiem':
                godzina = str(8)
            elif wybor_audio == 'dziewięć':
                godzina = str(9)
            elif wybor_audio == 'dziesięć':
                godzina = str(10)
            elif wybor_audio == 'jedenaście':
                godzina = str(11)
            elif wybor_audio == 'dwanaście':
                godzina = str(12)
            elif wybor_audio == 'trzynaście':
                godzina = str(13)
            elif wybor_audio == 'czternaście':
                godzina = str(14)
            elif wybor_audio == 'piętnaście':
                godzina = str(15)
            elif wybor_audio == 'szesnaście':
                godzina = str(16)
            elif wybor_audio == 'siedemnaście':
                godzina = str(17)
            elif wybor_audio == 'osiemnaście':
                godzina = str(18)
            elif wybor_audio == 'dziewiętnaście':
                godzina = str(19)
            elif wybor_audio == 'dwadzieścia':
                godzina = str(20)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if godzina == str(6):
                print('Wybrano godzinę 6:00')
                mow('Wybrano godzinę szóstą')
            elif godzina == str(7):
                print('Wybrano godzinę 7:00.')
                mow('Wybrano godzinę siódmą.')
            elif godzina == str(8):
                print('Wybrano godzinę 8:00.')
                mow('Wybrano godzinę ósmą.')
            elif godzina == str(9):
                print('Wybrano godzinę 9:00.')
                mow('Wybrano godzinę dziewiątą.')
            elif godzina == str(10):
                print('Wybrano godzinę 10:00.')
                mow('Wybrano godzinę dziesiątą.')
            elif godzina == str(11):
                print('Wybrano godzinę 11:00.')
                mow('Wybrano godziną jedenastą.')
            elif godzina == str(12):
                print('Wybrano godzinę 12:00.')
                mow('Wybrano godzinę dwunastą.')
            elif godzina == str(13):
                print('Wybrano godzinę 13:00.')
                mow('Wybrano godzinę trzynastą.')
            elif godzina == str(14):
                print('Wybrano godzinę 14:00.')
                mow('Wybrano godzinę czternastą.')
            elif godzina == str(15):
                print('Wybrano godzinę 15:00.')
                mow('Wybrano godzinę piętnastą.')
            elif godzina == str(16):
                print('Wybrano godzinę 16:00.')
                mow('Wybrano godzinę szesnastą.')
            elif godzina == str(17):
                print('Wybrano godzinę 17:00.')
                mow('Wybrano godzinę siedemnastą.')
            elif godzina == str(18):
                print('Wybrano godzinę 18:00.')
                mow('Wybrano godzinę osiemnastą.')
            elif godzina == str(19):
                print('Wybrano godzinę 19:00.')
                mow('Wybrano godzinę dziewiętnastą.')
            elif godzina == str(20):
                print('Wybrano godzinę 20:00.')
                mow('Wybrano godzinę dwudziestą.')
            else:
                wybor1Godzina()
            wybor1()
        else:
            print('Proszę wybrać odpowiednią godzinę. ')
            mow('Proszę wybrać odpowiednią godzinę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor1():
    zajety = 0
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin:
                    if element[0] == dzien:
                        if element[1] == godzina:
                            print('\n' + 'Tor w tym terminie jest zajęty.' + '\n\n')
                            mow('Tor w tym terminie jest zajęty.')
                            zajety = 1
                            intro()
                if zajety == 0:
                    print('\n' + 'Tory o tej godzinie są dostępne.' + '\n')
                    mow('Tory o tej godzinie są dostępne.')
                    print('\n' + 'Powiedz: ' + '\n'
                          '1 - aby zarezerwować tor.' + '\n' +
                          '2 - aby zamówic zajęcia z instruktorem.' + '\n' +
                          '3 - aby wrócić do menu glownego.' + '\n')
                    mow('Powiedz 1 aby zarezerwowac tor.')
                    mow('Powiedz 2 aby zamowic zajecia z instruktorem.')
                    mow('Powiedz 3 aby wrocic do menu glownego.')
                    print('Słucham...' + '\n')
                    mow('Słucham')
                    wybor1_2()
            else:
                print('\n' + 'Termin niedostępny. '+ '\n'
                             'Powiedz: ' + '\n'
                             '1 - aby wybrać inny termin. ' + '\n'
                             '2 - aby wrócić do menu głównego.' + '\n')
                mow('Termin niedostępny. Powiedz 1 aby wybrać inny termin, '
                    'powiedz 2 aby wrócic do menu głównego.')
                wybor1_3()
    else:
        print('Potrzebna liczba!' + '\n')
        mow('Potrzebna liczba')
        wybor1DzienPrinty()


def wybor1_2():
    wybor_inna_opcja = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
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
                    wybor3Printy()
                if wybor_inna_opcja == str(2):
                    wybor2Printy()
                if wybor_inna_opcja == str(3):
                    intro()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor1_2()
        elif wybor_awaryjny_input == str('2'):
            wybor_inna_opcja = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
            if wybor_audio == 'jeden':
                wybor_inna_opcja = str(1)
            elif wybor_audio == '1':
                wybor_inna_opcja = str(1)
            elif wybor_audio == '2':
                wybor_inna_opcja = str(2)
            elif wybor_audio == '3':
                wybor_inna_opcja = str(3)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_inna_opcja == str(1):
                wybor3()
            if wybor_inna_opcja == str(2):
                wybor2()
            if wybor_inna_opcja == str(3):
                intro()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor1_3():
    wybor_inna_opcja = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                # print(wybor_audio)
                if wybor_audio == 'jeden':
                    wybor_inna_opcja = str(1)
                elif wybor_audio == '1':
                    wybor_inna_opcja = str(1)
                elif wybor_audio == '2':
                    wybor_inna_opcja = str(2)
                else:
                    wybor1_3()
                if wybor_inna_opcja == str(1):
                    wybor1()
                if wybor_inna_opcja == str(2):
                    intro()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor1_3()
        elif wybor_awaryjny_input == str('2'):
            wybor_inna_opcja = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
            # print(wybor_audio)
            if wybor_audio == 'jeden':
                wybor_inna_opcja = str(1)
            elif wybor_audio == '1':
                wybor_inna_opcja = str(1)
            elif wybor_audio == '2':
                wybor_inna_opcja = str(2)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_inna_opcja == str(1):
                wybor1()
            if wybor_inna_opcja == str(2):
                intro()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor2Printy():
    print('\n' + 'Powiedz:' + '\n' +
          '1 - Aby wybrać poziom początkujący.' + '\n' +
          '2 - Aby wybrać poziom średniozaawansowany.' + '\n' +
          '3 - Aby wybrać poziom zaawansowany.' + '\n')
    mow('Powiedz: '
        '1 aby wybrać poziom początkujący. '
        '2 aby wybrać poziom średniozaawansowany. '
        '3 aby wybrać poziom zaawansowany. ')
    print('Słucham...' + '\n')
    mow('Słucham')
    wybor2()


def wybor2():
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                wybor_zaaw = ''
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
                    print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom początkujacy')
                    mow('Wybrano poziom początkujący.')
                    poziom_zaaw.append(wybor_zaaw)
                    # print(poziom_zaaw)
                    wybor3Printy()
                if wybor_zaaw == str(2):
                    print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom średniozaawansowany')
                    mow('Wybrano poziom średniozaawansowany.')
                    poziom_zaaw.append(wybor_zaaw)
                    # print(poziom_zaaw)
                    wybor3Printy()
                if wybor_zaaw == str(3):
                    print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom zaawansowany')
                    mow('Wybrano poziom zaawansowany.')
                    poziom_zaaw.append(wybor_zaaw)
                    # print(poziom_zaaw)
                    wybor3Printy()
                else:
                    print('\n' + 'Proszę wybrać odpowiednią liczbę.' + '\n' + '\n')
                    mow('Proszę wybrać odpowiednią liczbę.')
                    wybor2Printy()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor2()
        elif wybor_awaryjny_input == str('2'):
            wybor_audio = input('Którą opcję wybierasz?\n')
            wybor_zaaw = ''
            if wybor_audio == 'jeden':
                wybor_zaaw = str(1)
            elif wybor_audio == '1':
                wybor_zaaw = str(1)
            elif wybor_audio == '2':
                wybor_zaaw = str(2)
            elif wybor_audio == '3':
                wybor_zaaw = str(3)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_zaaw == str(1):
                print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom początkujacy')
                mow('Wybrano poziom początkujący.')
                poziom_zaaw.append(wybor_zaaw)
                # print(poziom_zaaw)
                wybor3Printy()
            if wybor_zaaw == str(2):
                print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom średniozaawansowany')
                mow('Wybrano poziom średniozaawansowany.')
                poziom_zaaw.append(wybor_zaaw)
                # print(poziom_zaaw)
                wybor3Printy()
            if wybor_zaaw == str(3):
                print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom zaawansowany')
                mow('Wybrano poziom zaawansowany.')
                poziom_zaaw.append(wybor_zaaw)
                # print(poziom_zaaw)
                wybor3Printy()
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę.' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor2Printy()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor3Printy():
    print('Otwieram rezerwację toru.')
    mow('Otwieram rezerwację toru.')
    wybor3DzienPrinty()


def wybor3DzienPrinty():
    print('\n' + 'Na jaki dzień tygodnia zarezerwować tor? (wybór od poniedziałku do niedzieli)')
    mow('Na jaki dzień tygodnia zarezerwować tor? (wybór od poniedziałku do niedzieli)')
    print('\n' + 'Podaj dzień: ')
    mow('Podaj dzień.')
    wybor3Dzien()


def wybor3Dzien():
    global dzien
    dzien = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
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
                elif wybor_audio == 'Poniedziałek':
                    dzien = str(1)
                elif wybor_audio == 'Wtorek':
                    dzien = str(2)
                elif wybor_audio == 'Środa':
                    dzien = str(3)
                elif wybor_audio == 'Czwartek':
                    dzien = str(4)
                elif wybor_audio == 'Piątek':
                    dzien = str(5)
                elif wybor_audio == 'Sobota':
                    dzien = str(6)
                elif wybor_audio == 'Niedziela':
                    dzien = str(7)
                else:
                    wybor3Dzien()
                if dzien == str(1):
                    print('Wybrano poniedziałek.')
                    mow('Wybrano poniedziałek.')
                elif dzien == str(2):
                    print('Wybrano wtorek.')
                    mow('Wybrano wtorek.')
                elif dzien == str(3):
                    print('Wybrano środę.')
                    mow('Wybrano środę.')
                elif dzien == str(4):
                    print('Wybrano czwartek.')
                    mow('Wybrano czwartek.')
                elif dzien == str(5):
                    print('Wybrano piątek')
                    mow('Wybrano piątek')
                elif dzien == str(6):
                    print('Wybrano sobotę.')
                    mow('Wybrano sobotę.')
                elif dzien == str(7):
                    print('Wybrano niedzielę.')
                    mow('Wybrano niedzielę.')
                else:
                    wybor3Dzien()
                wybor3GodzinaPrinty()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor3Dzien()
        elif wybor_awaryjny_input == str('2'):
            global dzien
            dzien = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
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
            elif wybor_audio == 'Poniedziałek':
                dzien = str(1)
            elif wybor_audio == 'Wtorek':
                dzien = str(2)
            elif wybor_audio == 'Środa':
                dzien = str(3)
            elif wybor_audio == 'Czwartek':
                dzien = str(4)
            elif wybor_audio == 'Piątek':
                dzien = str(5)
            elif wybor_audio == 'Sobota':
                dzien = str(6)
            elif wybor_audio == 'Niedziela':
                dzien = str(7)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if dzien == str(1):
                print('Wybrano poniedziałek.')
                mow('Wybrano poniedziałek.')
            elif dzien == str(2):
                print('Wybrano wtorek.')
                mow('Wybrano wtorek.')
            elif dzien == str(3):
                print('Wybrano środę.')
                mow('Wybrano środę.')
            elif dzien == str(4):
                print('Wybrano czwartek.')
                mow('Wybrano czwartek.')
            elif dzien == str(5):
                print('Wybrano piątek')
                mow('Wybrano piątek')
            elif dzien == str(6):
                print('Wybrano sobotę.')
                mow('Wybrano sobotę.')
            elif dzien == str(7):
                print('Wybrano niedzielę.')
                mow('Wybrano niedzielę.')
            else:
                wybor3Dzien()
            wybor3GodzinaPrinty()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor3GodzinaPrinty():
    print('\n' + 'Podaj godzinę (tylko pelne godziny od 6 do 20 godziny): ' + '\n')
    mow('Podaj godzinę, obowiązują tylko pełne godziny od szóstej do dwudziestej. ')
    print('Słucham...')
    mow('Słucham')
    wybor3Godzina()


def wybor3Godzina():
    global godzina
    godzina = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
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
                elif wybor_audio == 'pietnasta':
                    godzina = str(15)
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
                elif wybor_audio == '6':
                    godzina = str(6)
                elif wybor_audio == '7':
                    godzina = str(7)
                elif wybor_audio == '8':
                    godzina = str(8)
                elif wybor_audio == '9':
                    godzina = str(9)
                elif wybor_audio == '10':
                    godzina = str(10)
                elif wybor_audio == '11':
                    godzina = str(11)
                elif wybor_audio == '12':
                    godzina = str(12)
                elif wybor_audio == '13':
                    godzina = str(13)
                elif wybor_audio == '14':
                    godzina = str(14)
                elif wybor_audio == '15':
                    godzina = str(15)
                elif wybor_audio == '16':
                    godzina = str(16)
                elif wybor_audio == '17':
                    godzina = str(17)
                elif wybor_audio == '18':
                    godzina = str(18)
                elif wybor_audio == '19':
                    godzina = str(19)
                elif wybor_audio == '20':
                    godzina = str(20)
                elif wybor_audio == 'sześć':
                    godzina = str(6)
                elif wybor_audio == 'siedem':
                    godzina = str(7)
                elif wybor_audio == 'osiem':
                    godzina = str(8)
                elif wybor_audio == 'dziewięć':
                    godzina = str(9)
                elif wybor_audio == 'dziesięć':
                    godzina = str(10)
                elif wybor_audio == 'jedenaście':
                    godzina = str(11)
                elif wybor_audio == 'dwanaście':
                    godzina = str(12)
                elif wybor_audio == 'trzynaście':
                    godzina = str(13)
                elif wybor_audio == 'czternaście':
                    godzina = str(14)
                elif wybor_audio == 'piętnaście':
                    godzina = str(15)
                elif wybor_audio == 'szesnaście':
                    godzina = str(16)
                elif wybor_audio == 'siedemnaście':
                    godzina = str(17)
                elif wybor_audio == 'osiemnaście':
                    godzina = str(18)
                elif wybor_audio == 'dziewiętnaście':
                    godzina = str(19)
                elif wybor_audio == 'dwadzieścia':
                    godzina = str(20)
                else:
                    wybor3Godzina()
                if godzina == str(6):
                    print('Wybrano godzinę 6:00')
                    mow('Wybrano godzinę szóstą')
                elif godzina == str(7):
                    print('Wybrano godzinę 7:00.')
                    mow('Wybrano godzinę siódmą.')
                elif godzina == str(8):
                    print('Wybrano godzinę 8:00.')
                    mow('Wybrano godzinę ósmą.')
                elif godzina == str(9):
                    print('Wybrano godzinę 9:00.')
                    mow('Wybrano godzinę dziewiątą.')
                elif godzina == str(10):
                    print('Wybrano godzinę 10:00.')
                    mow('Wybrano godzinę dziesiątą.')
                elif godzina == str(11):
                    print('Wybrano godzinę 11:00.')
                    mow('Wybrano godziną jedenastą.')
                elif godzina == str(12):
                    print('Wybrano godzinę 12:00.')
                    mow('Wybrano godzinę dwunastą.')
                elif godzina == str(13):
                    print('Wybrano godzinę 13:00.')
                    mow('Wybrano godzinę trzynastą.')
                elif godzina == str(14):
                    print('Wybrano godzinę 14:00.')
                    mow('Wybrano godzinę czternastą.')
                elif godzina == str(15):
                    print('Wybrano godzinę 15:00.')
                    mow('Wybrano godzinę piętnastą.')
                elif godzina == str(16):
                    print('Wybrano godzinę 16:00.')
                    mow('Wybrano godzinę szesnastą.')
                elif godzina == str(17):
                    print('Wybrano godzinę 17:00.')
                    mow('Wybrano godzinę siedemnastą.')
                elif godzina == str(18):
                    print('Wybrano godzinę 18:00.')
                    mow('Wybrano godzinę osiemnastą.')
                elif godzina == str(19):
                    print('Wybrano godzinę 19:00.')
                    mow('Wybrano godzinę dziewiętnastą.')
                elif godzina == str(20):
                    print('Wybrano godzinę 20:00.')
                    mow('Wybrano godzinę dwudziestą.')
                else:
                    wybor3Godzina()
                wybor3()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor3Godzina()
        elif wybor_awaryjny_input == str('2'):
            global godzina
            godzina = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
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
            elif wybor_audio == 'pietnasta':
                godzina = str(15)
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
            elif wybor_audio == '6':
                godzina = str(6)
            elif wybor_audio == '7':
                godzina = str(7)
            elif wybor_audio == '8':
                godzina = str(8)
            elif wybor_audio == '9':
                godzina = str(9)
            elif wybor_audio == '10':
                godzina = str(10)
            elif wybor_audio == '11':
                godzina = str(11)
            elif wybor_audio == '12':
                godzina = str(12)
            elif wybor_audio == '13':
                godzina = str(13)
            elif wybor_audio == '14':
                godzina = str(14)
            elif wybor_audio == '15':
                godzina = str(15)
            elif wybor_audio == '16':
                godzina = str(16)
            elif wybor_audio == '17':
                godzina = str(17)
            elif wybor_audio == '18':
                godzina = str(18)
            elif wybor_audio == '19':
                godzina = str(19)
            elif wybor_audio == '20':
                godzina = str(20)
            elif wybor_audio == 'sześć':
                godzina = str(6)
            elif wybor_audio == 'siedem':
                godzina = str(7)
            elif wybor_audio == 'osiem':
                godzina = str(8)
            elif wybor_audio == 'dziewięć':
                godzina = str(9)
            elif wybor_audio == 'dziesięć':
                godzina = str(10)
            elif wybor_audio == 'jedenaście':
                godzina = str(11)
            elif wybor_audio == 'dwanaście':
                godzina = str(12)
            elif wybor_audio == 'trzynaście':
                godzina = str(13)
            elif wybor_audio == 'czternaście':
                godzina = str(14)
            elif wybor_audio == 'piętnaście':
                godzina = str(15)
            elif wybor_audio == 'szesnaście':
                godzina = str(16)
            elif wybor_audio == 'siedemnaście':
                godzina = str(17)
            elif wybor_audio == 'osiemnaście':
                godzina = str(18)
            elif wybor_audio == 'dziewiętnaście':
                godzina = str(19)
            elif wybor_audio == 'dwadzieścia':
                godzina = str(20)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if godzina == str(6):
                print('Wybrano godzinę 6:00')
                mow('Wybrano godzinę szóstą')
            elif godzina == str(7):
                print('Wybrano godzinę 7:00.')
                mow('Wybrano godzinę siódmą.')
            elif godzina == str(8):
                print('Wybrano godzinę 8:00.')
                mow('Wybrano godzinę ósmą.')
            elif godzina == str(9):
                print('Wybrano godzinę 9:00.')
                mow('Wybrano godzinę dziewiątą.')
            elif godzina == str(10):
                print('Wybrano godzinę 10:00.')
                mow('Wybrano godzinę dziesiątą.')
            elif godzina == str(11):
                print('Wybrano godzinę 11:00.')
                mow('Wybrano godziną jedenastą.')
            elif godzina == str(12):
                print('Wybrano godzinę 12:00.')
                mow('Wybrano godzinę dwunastą.')
            elif godzina == str(13):
                print('Wybrano godzinę 13:00.')
                mow('Wybrano godzinę trzynastą.')
            elif godzina == str(14):
                print('Wybrano godzinę 14:00.')
                mow('Wybrano godzinę czternastą.')
            elif godzina == str(15):
                print('Wybrano godzinę 15:00.')
                mow('Wybrano godzinę piętnastą.')
            elif godzina == str(16):
                print('Wybrano godzinę 16:00.')
                mow('Wybrano godzinę szesnastą.')
            elif godzina == str(17):
                print('Wybrano godzinę 17:00.')
                mow('Wybrano godzinę siedemnastą.')
            elif godzina == str(18):
                print('Wybrano godzinę 18:00.')
                mow('Wybrano godzinę osiemnastą.')
            elif godzina == str(19):
                print('Wybrano godzinę 19:00.')
                mow('Wybrano godzinę dziewiętnastą.')
            elif godzina == str(20):
                print('Wybrano godzinę 20:00.')
                mow('Wybrano godzinę dwudziestą.')
            else:
                wybor3Godzina()
            wybor3()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor3():
    global poziom_zaaw_mow
    lista_uzyt = []
    imie = ''
    nazwisko = ''
    print('Aby rozpoczac rezerwacje, wpisz najpierw swoje imie i wcisnij enter:' + '\n')
    mow('Aby rozpocząć rezerwację, wpisz najpierw swoie imię i wciśnij enter.')
    imie = input('Imię: ')
    print('Za chwilę wpisz swoje nazwisko i wcisnij enter:' + '\n')
    mow('Za chwilę wpisz swoje nazwisko i wciśnij enter.')
    nazwisko = input('Nazwisko: ')
    #for line in imie and nazwisko:
    #    string = line.replace('','')
    imie_lista = list(imie)
    for i, n in enumerate(imie_lista):
        if n == str('ą'):
            imie_lista[i] = str('a')
        elif n == str('ć'):
            imie_lista[i] = str('c')
        elif n == str('ę'):
            imie_lista[i] = str('e')
        elif n == str('ł'):
            imie_lista[i] = str('l')
        elif n == str('ń'):
            imie_lista[i] = str('n')
        elif n == str('ó'):
            imie_lista[i] = str('o')
        elif n == str('ś'):
            imie_lista[i] = str('s')
        elif n == str('ź'):
            imie_lista[i] = str('z')
        elif n == str('ż'):
            imie_lista[i] = str('z')
        elif n == str('Ą'):
            imie_lista[i] = str('A')
        elif n == str('Ć'):
            imie_lista[i] = str('C')
        elif n == str('Ę'):
            imie_lista[i] = str('E')
        elif n == str('Ł'):
            imie_lista[i] = str('L')
        elif n == str('Ń'):
            imie_lista[i] = str('N')
        elif n == str('Ó'):
            imie_lista[i] = str('O')
        elif n == str('Ś'):
            imie_lista[i] = str('S')
        elif n == str('Ż'):
            imie_lista[i] = str('Z')
        elif n == str('Ź'):
            imie_lista[i] = str('Z')
    global imie_bezpz
    imie_bezpz = ''.join(imie_lista)
    nazwisko_lista = list(nazwisko)
    for i, n in enumerate(nazwisko_lista):
        if n == str('ą'):
            nazwisko_lista[i] = str('a')
        elif n == str('ć'):
            nazwisko_lista[i] = str('c')
        elif n == str('ę'):
            nazwisko_lista[i] = str('e')
        elif n == str('ł'):
            nazwisko_lista[i] = str('l')
        elif n == str('ń'):
            nazwisko_lista[i] = str('n')
        elif n == str('ó'):
            nazwisko_lista[i] = str('o')
        elif n == str('ś'):
            nazwisko_lista[i] = str('s')
        elif n == str('ź'):
            nazwisko_lista[i] = str('z')
        elif n == str('ż'):
            nazwisko_lista[i] = str('z')
        elif n == str('Ą'):
            nazwisko_lista[i] = str('A')
        elif n == str('Ć'):
            nazwisko_lista[i] = str('C')
        elif n == str('Ę'):
            nazwisko_lista[i] = str('E')
        elif n == str('Ł'):
            nazwisko_lista[i] = str('L')
        elif n == str('Ń'):
            nazwisko_lista[i] = str('N')
        elif n == str('Ó'):
            nazwisko_lista[i] = str('O')
        elif n == str('Ś'):
            nazwisko_lista[i] = str('S')
        elif n == str('Ż'):
            nazwisko_lista[i] = str('Z')
        elif n == str('Ź'):
            nazwisko_lista[i] = str('Z')
    global nazwisko_bezpz
    nazwisko_bezpz = ''.join(nazwisko_lista)
    zajety = 0
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin:
                    if element[0] == str(dzien):
                        if element[1] == str(godzina):
                            zajety = 1
                            print('\n' + 'Termin niedostępny. ' + '\n'
                                         'Powiedz: ' + '\n'
                                         '1 - aby wybrać inny termin. ' + '\n'
                                         '2 - aby wrócić do menu głównego.' + '\n')
                            mow('Termin niedostępny. Powiedz jeden aby wybrać inny termin,'
                                'Powiedz dwa aby wrócić do menu głównego.')
                            wybor3_1()
                if zajety == 0:
                    # print(str(poziom_zaaw))
                    godzina_mow = ''
                    if godzina == '6':
                        godzina_mow = str('od szóstej do siódmej.')
                    elif godzina == '7':
                        godzina_mow = str('od siódmej do ósmej.')
                    elif godzina == '8':
                        godzina_mow = str('od ósmej do dziewiątej.')
                    elif godzina == '9':
                        godzina_mow = str('od dziewiątej do dziesiątej.')
                    elif godzina == '10':
                        godzina_mow = str('od dziesiątej do jedenastej.')
                    elif godzina == '11':
                        godzina_mow = str('od jedenastej do dwunastej.')
                    elif godzina == '12':
                        godzina_mow = str('od dwunastej do trzynastej.')
                    elif godzina == '13':
                        godzina_mow = str('od trzynastej do czternastej.')
                    elif godzina == '14':
                        godzina_mow = str('od czternastej do piętnastej')
                    elif godzina == '15':
                        godzina_mow = str('od piętnastej do szesnastej.')
                    elif godzina == '16':
                        godzina_mow = str('od szesnastej do siedemnastej.')
                    elif godzina == '17':
                        godzina_mow = str('od siedemnastej do osiemnastej.')
                    elif godzina == '18':
                        godzina_mow = str('od osiemnastej do dziewiętnastej.')
                    elif godzina == '19':
                        godzina_mow = str('od dziewiętnastej do dwudziestej.')
                    elif godzina == '20':
                        godzina_mow = str('od dwudziestej do dwudziestej pierwszej')
                    print('\n' + 'Dziękujemy za skorzystanie z usługi użytkowniku' + ' ' + imie + ' ' + nazwisko + '!')
                    mow('Dziękujemy za skorzystanie z usługi użytkowniku' + ' ' + imie + ' ' + nazwisko + '!')
                    if bool(poziom_zaaw) is True:
                        print('\n' + 'Wybrano następujące dni, godziny i poziom zaawansowania:')
                        mow('Wybrano następujące dni, godziny i poziom zaawansowania:')
                    if bool(poziom_zaaw) is False:
                        print('\n' + 'Wybrano następujace dni i godziny:')
                        mow('Wybrano następujące dni i godziny')
                    poziom_zaaw_print = ''
                    if bool(poziom_zaaw) is True:
                        poziom_zaaw_mow = ''
                        if poziom_zaaw[0] == '1':
                            poziom_zaaw_mow = str('początkujący')
                        if poziom_zaaw[0] == '2':
                            poziom_zaaw_mow = str('średniozaawansowany')
                        if poziom_zaaw[0] == '3':
                            poziom_zaaw_mow = str('zaawansowany')
                        poziom_zaaw_bool = bool(poziom_zaaw)
                        if poziom_zaaw_bool is True:
                            poziom_zaaw_print = str('Poziom zaawansowania: ' + poziom_zaaw_mow)
                        else:
                            poziom_zaaw_print = str('')
                    godzina_print = ''
                    if godzina == '6':
                        godzina_print = str('Od 6:00 do 7:00')
                    elif godzina == '7':
                        godzina_print = str('Od 7:00 do 8:00')
                    elif godzina == '8':
                        godzina_print = str('Od 8:00 do 9:00')
                    elif godzina == '9':
                        godzina_print = str('Od 90:00 do 10:00')
                    elif godzina == '10':
                        godzina_print = str('Od 10:00 do 11:00')
                    elif godzina == '11':
                        godzina_print = str('Od 11:00 do 12:00')
                    elif godzina == '12':
                        godzina_print = str('Od 12:00 do 13:00')
                    elif godzina == '13':
                        godzina_print = str('Od 13:00 do 14:00')
                    elif godzina == '14':
                        godzina_print = str('Od 14:00 do 15:00')
                    elif godzina == '15':
                        godzina_print = str('Od 15:00 do 16:00')
                    elif godzina == '16':
                        godzina_print = str('Od 16:00 do 17:00')
                    elif godzina == '17':
                        godzina_print = str('Od 17:00 do 18:00')
                    elif godzina == '18':
                        godzina_print = str('Od 18:00 do 19:00')
                    elif godzina == '19':
                        godzina_print = str('Od 19:00 do 20:00')
                    elif godzina == '20':
                        godzina_print = str('Od 20:00 do 21:00')
                    if dzien == str(1):
                        print('Poniedziałek godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Poniedziałek godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(2):
                        print('Wtorek godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Wtorek godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(3):
                        print('Środa godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Środa godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(4):
                        print('Czwartek godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Czwartek godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(5):
                        print('Piątek godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Piątek godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(6):
                        print('Sobota godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Sobota godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    if dzien == str(7):
                        print('Niedziela godzina:' + ' ' + godzina_print + '\n' + poziom_zaaw_print)
                        mow('Niedziela godzina:' + ' ' + godzina_mow + poziom_zaaw_print)
                    potwierdzenie_printy()
            else:
                print('\n' + 'Termin niedostępny. ' + '\n'
                             'Powiedz: ' + '\n'
                             '1 - aby wybrać inny termin. ' + '\n'
                             '2 - aby wrócić do menu głównego.' + '\n')
                mow('Termin niedostępny. '
                    'Powiedz jeden aby wybrać inny termin,'
                    'Powiedz dwa aby wrócić do menu głównego.')
                wybor3_2()
    else:
        print('Potrzebna liczba!' + '\n')
        mow('Potrzebna liczba!')
        wybor3()


def potwierdzenie_printy():
    print('\n' + 'Powiedz: '
                 '\nTak - jeśli dane są poprawne.'
                 '\nNie - aby wrócić do menu i ponownie spróbować wprowadzić dane.')
    mow('Powiedz: Tak - jeśli dane są poprawne. Nie - aby wrócić do menu i ponownie spróbować wprowadzić dane.')
    potwierdzenie()


def potwierdzenie():
    lista_uzyt = []
    imie = ''
    nazwisko = ''
    wybor_audio = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                # print(wybor_audio)
                wybor_audio_potwierdzenie = ''
                if wybor_audio == 'tak':
                    wybor_audio_potwierdzenie = str(1)
                elif wybor_audio == 'Tak':
                    wybor_audio_potwierdzenie = str(1)
                elif wybor_audio == 'nie':
                    wybor_audio_potwierdzenie = str(2)
                elif wybor_audio == 'Nie':
                    wybor_audio_potwierdzenie = str(2)
                else:
                    potwierdzenie()
                if wybor_audio_potwierdzenie == str(1):
                    lista_uzyt.append(dzien)
                    # print(lista_uzyt)
                    lista_uzyt.append(godzina)
                    # print(lista_uzyt)
                    termin.append(lista_uzyt)
                    # print(termin)
                    outfile = open('dane.txt', 'a', encoding='utf-8')
                    outfile.write(dzien + '\t' + godzina + '\t' + imie_bezpz + '\t'
                                  + nazwisko_bezpz + '\t' + str(poziom_zaaw) + '\n')
                    outfile.close()
                    print('Dodano rezerwację.')
                    mow('Dodano rezerwację.')
                    list.clear(poziom_zaaw)
                    dziekiPrinty()
                elif wybor_audio_potwierdzenie == str(2):
                    if bool(poziom_zaaw) is True:
                        list.clear(poziom_zaaw)
                        intro()
                    if bool(poziom_zaaw) is False:
                        intro()
                else:
                    potwierdzenie()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            potwierdzenie()
        elif wybor_awaryjny_input == str('2'):
            wybor_audio = input('Którą opcję wybierasz?\n')
            wybor_audio_potwierdzenie = ''
            if wybor_audio == 'tak':
                wybor_audio_potwierdzenie = str(1)
            elif wybor_audio == 'Tak':
                wybor_audio_potwierdzenie = str(1)
            elif wybor_audio == 'nie':
                wybor_audio_potwierdzenie = str(2)
            elif wybor_audio == 'Nie':
                wybor_audio_potwierdzenie = str(2)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_audio_potwierdzenie == str(1):
                lista_uzyt.append(dzien)
                # print(lista_uzyt)
                lista_uzyt.append(godzina)
                # print(lista_uzyt)
                termin.append(lista_uzyt)
                # print(termin)
                outfile = open('dane.txt', 'a', encoding='utf-8')
                outfile.write(dzien + '\t' + godzina + '\t' + imie_bezpz + '\t'
                              + nazwisko_bezpz + '\t' + str(poziom_zaaw) + '\n')
                outfile.close()
                print('Dodano rezerwację.')
                mow('Dodano rezerwację.')
                list.clear(poziom_zaaw)
                dziekiPrinty()
            elif wybor_audio_potwierdzenie == str(2):
                if bool(poziom_zaaw) is True:
                    list.clear(poziom_zaaw)
                    intro()
                if bool(poziom_zaaw) is False:
                    intro()
            else:
                potwierdzenie()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor3_1():
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                if wybor_audio == 'jeden':
                    wybor_inna_opcja_3 = str(1)
                elif wybor_audio == '1':
                    wybor_inna_opcja_3 = str(1)
                elif wybor_audio == '2':
                    wybor_inna_opcja_3 = str(2)
                else:
                    wybor3_1()
                if wybor_inna_opcja_3 == str(1):
                    wybor3Printy()
                if wybor_inna_opcja_3 == str(2):
                    intro()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor3_1()
        elif wybor_awaryjny_input == str('2'):
            wybor_inna_opcja_3 = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
            if wybor_audio == 'jeden':
                wybor_inna_opcja_3 = str(1)
            elif wybor_audio == '1':
                wybor_inna_opcja_3 = str(1)
            elif wybor_audio == '2':
                wybor_inna_opcja_3 = str(2)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_inna_opcja_3 == str(1):
                wybor3Printy()
            if wybor_inna_opcja_3 == str(2):
                intro()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def wybor3_2():
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                if wybor_audio == 'jeden':
                    wybor_inna_opcja_4 = str(1)
                elif wybor_audio == '1':
                    wybor_inna_opcja_4 = str(1)
                elif wybor_audio == '2':
                    wybor_inna_opcja_4 = str(2)
                else:
                    wybor3()
                if wybor_inna_opcja_4 == str(1):
                    if bool(poziom_zaaw) is True:
                        wybor2()
                    if bool(poziom_zaaw) is False:
                        wybor3Printy()
                if wybor_inna_opcja_4 == str(2):
                    intro()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:' 
              '\n1 aby spróbować ponownie.' 
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            wybor3_2()
        elif wybor_awaryjny_input == str('2'):
            wybor_inna_opcja_4 = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
            if wybor_audio == 'jeden':
                wybor_inna_opcja_4 = str(1)
            elif wybor_audio == '1':
                wybor_inna_opcja_4 = str(1)
            elif wybor_audio == '2':
                wybor_inna_opcja_4 = str(2)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_inna_opcja_4 == str(1):
                if bool(poziom_zaaw) is True:
                    wybor2()
                if bool(poziom_zaaw) is False:
                    wybor3Printy()
            if wybor_inna_opcja_4 == str(2):
                intro()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def stronainternetowa():
    webbrowser.open('https://posir.poznan.pl/obiekty/winogrady/plywalnia-kryta', new=0, autoraise=True)
    print('Otwarto przeglądarkę i stronę internetową.')
    mow('Otwarto przeglądarkę i stronę internetową.')
    intro()


def grafik():
    grafikzdjecie = PIL.Image.open('JPG/grafik.jpg')
    grafikzdjecie.show()
    print('Wyswietlono grafik.')
    mow('Wyświetlono grafik.')
    intro()


def dziekiPrinty():
    print('\nPowiedz 1 aby wrócić do menu głównego.\nPowiedz 2 aby wyświetlić motywującą wiadoomość.' + '\n')
    mow('Powiedz jeden aby wrócić do menu głównego.')
    mow('Powiedz dwa aby wyświetlić motywującą wiadomość.')
    print('Co chcesz zrobic?' + '\n'
          'Słucham...' + '\n')
    mow('Co chcesz zrobić? Słucham')
    dzieki()


def dzieki():
    wybor_inna_opcja_5 = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                if wybor_audio == 'jeden':
                    wybor_inna_opcja_5 = str(1)
                elif wybor_audio == '1':
                    wybor_inna_opcja_5 = str(1)
                elif wybor_audio == '2':
                    wybor_inna_opcja_5 = str(2)
                else:
                    dzieki()
                if wybor_inna_opcja_5 == str(1):
                    print('\n' + 'Wybrałeś numer: ' + wybor_inna_opcja_5 + '\n')
                    mow('Wybrałeś numer: ' + wybor_inna_opcja_5)
                    print('\n' + 'Wybrano powrót do menu.')
                    mow('Wybrano powrót do menu.')
                    time.sleep(1)
                    intro()
                if wybor_inna_opcja_5 == str(2):
                    print('\n' + 'Wybrałeś numer: ' + wybor_inna_opcja_5 + '\n')
                    mow('Wybrałeś numer: ' + wybor_inna_opcja_5)
                    plik = open('TEXT/motywacja.txt', "r", encoding='utf-8')
                    motywacja = plik.readlines()
                    plik.close()
                    losowe = random.choice(motywacja)
                    dawaj = losowe.strip()
                    krowa = cowsay.cow(dawaj)
                    print(krowa)
                    dawaj = losowe.strip()
                    mow(dawaj)
                    dziekiPrinty()
                else:
                    print('\n' + 'Proszę wybrać odpowiednia liczbe!1111' + '\n' + '\n')
                    mow('Proszę wybrać odpowiednią liczbę!')
                    dziekiPrinty()
            except:
                continue
    print('\nNie udało się rozpoznać mowy.')
    mow('Nie udało się rozpoznać mowy. ')

    def wybor_awaryjny():
        print('Wybierz:'
              '\n1 aby spróbować ponownie.'
              '\n2 aby wybrać opcję klawiaturą.')
        mow('Wybierz 1 - aby spróbować ponownie. '
            'Wybierz 2 - aby wybrać opcję klawiaturą.')
        wybor_awaryjny_input = input('Wybór: ')
        if wybor_awaryjny_input == str('1'):
            dziekiPrinty()
        elif wybor_awaryjny_input == str('2'):
            wybor_audio = input('Którą opcję wybierasz?\n')
            if wybor_audio == 'jeden':
                wybor_inna_opcja_5 = str(1)
            elif wybor_audio == '1':
                wybor_inna_opcja_5 = str(1)
            elif wybor_audio == '2':
                wybor_inna_opcja_5 = str(2)
            else:
                print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę.')
                wybor_awaryjny()
            if wybor_inna_opcja_5 == str(1):
                print('\n' + 'Wybrałeś numer: ' + wybor_inna_opcja_5 + '\n')
                mow('Wybrałeś numer: ' + wybor_inna_opcja_5)
                print('\n' + 'Wybrano powrót do menu.')
                mow('Wybrano powrót do menu.')
                time.sleep(1)
                intro()
            if wybor_inna_opcja_5 == str(2):
                print('\n' + 'Wybrałeś numer: ' + wybor_inna_opcja_5 + '\n')
                mow('Wybrałeś numer: ' + wybor_inna_opcja_5)
                plik = open('TEXT/motywacja.txt', "r", encoding='utf-8')
                motywacja = plik.readlines()
                plik.close()
                losowe = random.choice(motywacja)
                dawaj = losowe.strip()
                krowa = cowsay.cow(dawaj)
                print(krowa)
                dawaj = losowe.strip()
                mow(dawaj)
                dziekiPrinty()
            else:
                print('\n' + 'Prosze wybrać odpowiednia liczbe!' + '\n' + '\n')
                mow('Proszę wybrać odpowiednią liczbę!')
                dziekiPrinty()
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()


def haslop():
    haslo_pracownik = 'aestusp'
    print('\n' + 'Podaj haslo:' + '\n')
    podanehaslo = input()
    if podanehaslo == haslo_pracownik:
        print('Sprawdzanie hasła.')
        for x in range(0, 3):
            b = "." * x
            print(b, end="\r")
            time.sleep(1)
        panelpracownika()
    else:
        print('Niepoprawne haslo!')
        intro()


def hasloa():
    haslo_admin = 'aestusa'
    print('\n' + 'Podaj haslo:' + '\n')
    podanehaslo = input()
    if podanehaslo == haslo_admin:
        print('Sprawdzanie hasła.')
        for x in range(0, 3):
            b = "." * x
            print(b, end="\r")
            time.sleep(1)
        paneladministratora()
    else:
        print('Niepoprawne haslo!')
        intro()


def panelpracownika_vhelper():
    input('\n' + 'Wciśnij enter aby wyświetlić panel pracownika.' + '\n')
    panelpracownika()


def panelpracownika():
    pp = input('\n' + 'Wybierz 1 aby dodać godziny wejscia i wyjscia, ' + '\n' +
                      'Wybierz 2 aby wyświetlić aktualne terminy pracy, ' + '\n' +
                      'Wybierz 3 aby wyświetlić historię usuniętych terminów pracy.' + '\n' +
                      'Wybierz 4 aby wrócić do głównego menu.' + '\n' + 'Wybór: ')
    if pp == str('1'):
        godziny_wejscia_i_wyjscia()
    elif pp == str('2'):
        drukowanie_termin_pracy()
    elif pp == str('3'):
        wyswietlanie_historii_usuwania_terminy()
    elif pp == str('4'):
        intro()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
        panelpracownika_vhelper()


def godziny_wejscia_i_wyjscia_menu():
    gwm = input('\n' + 'Wybierz 1 aby dodać zmianę. Wybierz 2 aby wrócić do panelu pracownika.' + '\n' + 'Wybór: ')
    if gwm == str('1'):
        godziny_wejscia_i_wyjscia()
    elif gwm == str('2'):
        panelpracownika()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
        godziny_wejscia_i_wyjscia_menu()


def godziny_wejscia_i_wyjscia():
    print('Aby dodać godziny pracy:')
    termin_pracy_pomocniczy = []
    lista_pomocnicza_godzin = []
    lista_pomocnicza_dni = []
    lista_pomocnicza_numeru_pracownika = []
    numer_pracownika = input('\n' + 'Podaj numer pracownika: ')
    miesiac_pracy = input('Podaj miesiąc pracy wejscia: ')
    dzien_pracy = input('Podaj dzień miesiąca wejscia: ')
    godzina_wej = input('Podaj godzinę wejscia: ')
    godzina_wyj = input('Podaj godzinę wyjscia: ')
    lista_pomocnicza_numeru_pracownika.append(numer_pracownika)
    lista_pomocnicza_dni.append(miesiac_pracy)
    lista_pomocnicza_dni.append(dzien_pracy)
    lista_pomocnicza_godzin.append(godzina_wej)
    lista_pomocnicza_godzin.append(godzina_wyj)
    termin_pracy_pomocniczy.append(lista_pomocnicza_numeru_pracownika)
    termin_pracy_pomocniczy.append(lista_pomocnicza_dni)
    termin_pracy_pomocniczy.append(lista_pomocnicza_godzin)
    print('\n' + 'Legenda: ' + '\n' +
          'Nr - numer pracownika' + '\n' +
          'M - miesiąc' + '\n' +
          'D - dzień' + '\n' +
          'S - start zmiany' + '\n' +
          'K - koniec zmiany')
    print('\n' + 'Id:',
          '\t',
          '[[Nr: ],',
          '[M: , D: ],',
          '[S:, K:]]')
    print('N:', '\t', termin_pracy_pomocniczy)
    sprawdzenie_danych = input('\n' + 'Sprawdź poprawnośc danych.' + '\n' + 'Jeśli dane są poprawne wybierz 1. ' +
                               '\n' + 'Aby porawić dane wybierz 2. ' + '\n' + 'Wybór: ')
    if sprawdzenie_danych == str('1'):
        termin_pracy.append(termin_pracy_pomocniczy)
        godziny_wejscia_i_wyjscia_menu()
    elif sprawdzenie_danych == str('2'):
        godziny_wejscia_i_wyjscia()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
        panelpracownika()


def drukowanie_termin_pracy():
    print('\n' + 'Wyświetlanie terminów pracy:')
    if bool(termin_pracy) is False:
        print('Brak terminów do wyświetlenia.')
        panelpracownika()
    numery_wejsc_pomocniczy = [1 + n for n in range(len(termin_pracy))]
    numery_wejsc = {numery_wejsc_pomocniczy[i]: termin_pracy[i] for i in range(len(termin_pracy))}
    print('\n' + 'Legenda: ' + '\n' +
          'Nr - numer pracownika' + '\n' +
          'M - miesiąc' + '\n' +
          'D - dzień' + '\n' +
          'S - start zmiany' + '\n' +
          'K - koniec zmiany'
          )
    print('\n' + 'Id:',
          '\t',
          '[[Nr: ],',
          '[M: , D: ],',
          '[S:, K:]]')
    for a, b in numery_wejsc.items():
        print(a - 1,
              ':',
              '\t',
              b)
    panelpracownika_vhelper()


def wyswietlanie_historii_usuwania_terminy():
    if bool(termin_usunieto_pracowniczy) is False:
        print('\n' + 'Brak terminów do wyświetlenia.')
        panelpracownika()
    print('\n' + 'Legenda: ' + '\n' +
          'Nr - numer pracownika' + '\n' +
          'M - miesiąc' + '\n' +
          'D - dzień' + '\n' +
          'S - start zmiany' + '\n' +
          'K - koniec zmiany')
    print('Histora usuniętych terminów: ')
    print('\n' + 'Id:',
          '\t',
          '[[Nr: ],',
          '[M: , D: ],',
          '[S:, K:]]')
    numery_wejsc_usunietych_pomocniczy = [1 + n for n in range(len(termin_usunieto_pracowniczy))]
    numery_wejsc_usunietych = {numery_wejsc_usunietych_pomocniczy[i]: termin_usunieto_pracowniczy[i] for i in range(
        len(termin_usunieto_pracowniczy))}
    for a, b in numery_wejsc_usunietych.items():
        print(a - 1,
              ':',
              '\t',
              b)
    panelpracownika_vhelper()


def paneladministratora_vhelper():
    input('\n' + 'Wciśnij enter aby wyświetlić panel administratora.' + '\n')
    paneladministratora()


def paneladministratora():
    print('\n' + 'Witaj administratorze.')
    print('\n' + 'Wybierz:')
    print('1 - aby wyswietlic tabele.'
          '\n2 - aby rozpocząć usuwanie tabel.'
          '\n3 - aby usunąć wszystkie tabele.'
          '\n4 - aby wyświetlić usunięte tabele.'
          '\n5 - aby wydrukować historię usuniętych tabel do pliku zewnętrznego.'
          ###
          '\n6 - aby wyświetlić aktualne terminy pracy.'
          '\n7 - aby rozpocząć usuwanie terminów pracy.'
          '\n8 - aby usunąć wszystkie terminy pracy.'
          '\n9 - aby wyświetlić historię usuniętych terminów pracy.'
          '\n10 - aby wydrukować historię usuniętych terminów pracy do pliku zewnętrznego.'
          ###
          '\n11 - aby włączyć mowę.'
          '\n12 - aby wyłączyć mowe.'
          '\n13 - aby zakonczyc program.'
          '\n14 - aby wrocic do menu glownego.\n')
    wyboradmin = ''
    wyboradmin = input('Co chcesz zrobic?' + '\n' + 'Numer:')
    if wyboradmin == str(1):
        print('\n' + 'Tabele:')
        wyswietlanie_tabele_1()
    elif wyboradmin == str(2):
        print('\n' + 'Rozpoczynam usuwanie tabel.' + '\n')
        usuwanie_tabele_2()
    elif wyboradmin == str(3):
        print('\n' + 'Rozpoczynam usuwanie wszystkich tabel.' + '\n')
        czyszczenie_tabele_3()
    elif wyboradmin == str(4):
        print('\n' + 'Wyświetlam usunięte tabele.' + '\n')
        wyswietlanie_tabele_usuniete_4()
    elif wyboradmin == str(5):
        print('\n' + 'Drukuje historię usuniętych tabel do pliku zewnętrznego.' + '\n')
        drukowanie_tabele_usuniete_5()
    elif wyboradmin == str(6):
        print('\n' + 'Wyświetlam aktualne terminy pracy.' + '\n')
        wyswietlanie_terminu_6()
    elif wyboradmin == str(7):
        print('\n' + 'Rozpoczynam usuwanie terminów pracy. ' + '\n')
        usuwanie_terminu_7()
    elif wyboradmin == str(8):
        print('\n' + 'Rozpoczynam usuwanie wszystkich terminów pracy.' + '\n')
        czysczenie_terminu_8()
    elif wyboradmin == str(9):
        print('\n' + 'Wyświetlam historię usuniętych terminów pracy.' + '\n')
        wyswitlanie_terminu_usuniete_9()
    elif wyboradmin == str(10):
        print('\n' + 'Drukuje historię usuniętych terminów pracy do pliku zewnętrznego.' + '\n')
        drukowanie_terminu_usuniete_10()
    elif wyboradmin == str(11):
        print('\n' + 'Mowa włączona.' + '\n')
        wlacz_mowe_11()
    elif wyboradmin == str(12):
        print('\n' + 'Mowa wyłączona.' + '\n')
        wylacz_mowe_12()
    elif wyboradmin == str(13):
        print('\n' + 'Koncze program.' + '\n')
        end()
    elif wyboradmin == str(14):
        print('\n' + 'Wracam do menu.' + '\n')
        intro()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        paneladministratora()


def wyswietlanie_tabele_1():
    if bool(termin) is False:
        print('Brak terminów.')
        paneladministratora_vhelper()
    print('\n' + 'Legenda: ' + '\n' +
          'D - Dzień tygodnia' + '\n' +
          'G - godzina'
          )
    print('\n' + 'Id:',
          '\t',
          '[D: , G: ]',
          )
    numery_termin_pomocniczy = [1 + n for n in range(len(termin))]
    numery_termin = {numery_termin_pomocniczy[i]: termin[i] for i in range(len(termin))}
    for a, b in numery_termin.items():
        print(a - 1,
              ':',
              '\t',
              b)
    paneladministratora_vhelper()


def usuwanie_tabele_2():
    print('Legenda: ' + '\n' +
          'D - Dzień tygodnia' + '\n' +
          'G - godzina'
          )
    print('\n' + 'Id:',
          '\t',
          '[D: , G: ]',
          )
    numery_termin_pomocniczy = [1 + n for n in range(len(termin))]
    numery_termin = {numery_termin_pomocniczy[i]: termin[i] for i in range(len(termin))}
    for a, b in numery_termin.items():
        print(a - 1,
              ':',
              '\t',
              b)
    if bool(termin) is False:
        print('Brak terminów do usunięcia.')
        usuwanie_tabele_menu()
    print('\n' + 'Aby zrezygnować zostaw pusty wybór.')
    usun = input('Wybierz numer (Id:) do usunięcia: ')
    if usun.isdigit() and int(usun) >= 0:
        if int(usun) <= len(termin) - 1:
            usun_int = int(usun)
            termin_ktory_usunieto = termin.pop(usun_int)
            print('Termin który usunięto: ', termin_ktory_usunieto)
            termin_usunieto.insert(0, termin_ktory_usunieto)
            print('\n' + 'Legenda: ' + '\n' +
                  'D - Dzień tygodnia' + '\n' +
                  'G - godzina'
                  )
            print('Usunięto: ')
            print('\n' + 'Id:',
                  '\t',
                  '[D: , G: ]',
                  )
            numery_terminow_usunietych_pomocniczy = [1 + n for n in range(len(termin_usunieto))]
            numery_terminow_usunietych = {numery_terminow_usunietych_pomocniczy[i]: termin_usunieto[i]
                                          for i in range(len(termin_usunieto))}
            for a, b in numery_terminow_usunietych.items():
                print(a - 1,
                      ':',
                      '\t',
                      b)
            else:
                print('\n' + 'Pozostałe terminy: ')
                print('\n' + 'Id:',
                      '\t',
                      '[D: , G: ]',
                      )
                numery_termin_pomocniczy = [1 + n for n in range(len(termin))]
                numery_termin = {numery_termin_pomocniczy[i]: termin[i] for i in range(len(termin))}
                for a, b in numery_termin.items():
                    print(a - 1,
                          ':',
                          '\t',
                          b)
            usuwanie_tabele_menu()
        else:
            print('Brak terminów, lub podano nieodpowiednią liczbę.')
            usuwanie_tabele_menu()
    else:
        print('Brak terminów, lub podano nieodpowiednią liczbę.')
        usuwanie_tabele_menu()


def usuwanie_tabele_menu():
    powrot = input(
        '\n' + 'Aby usunąć termin wybierz 1.' + '\n' + 'Aby wrócic do panelu administratora wybierz 2.' + '\n')
    if powrot == str('1'):
        usuwanie_tabele_2()
    elif powrot == str('2'):
        paneladministratora()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n')
        usuwanie_tabele_menu()


def czyszczenie_tabele_3():
    potwierdzenie_czyszczenie = input('Aby usunąć wszystkie tabele wpisz komendę: "usun".' + '\n' + 'Komenda: ')
    if potwierdzenie_czyszczenie == str('usun'):
        print('Legenda: ' + '\n' +
              'D - Dzień tygodnia' + '\n' +
              'G - godzina'
              )
        print('\n' + 'Termiy które usunięto.')
        print('Id:',
              '\t',
              '[D: , G: ]',
              )
        numery_termin_pomocniczy = [1 + n for n in range(len(termin))]
        numery_termin = {numery_termin_pomocniczy[i]: termin[i] for i in range(len(termin))}
        for a, b in numery_termin.items():
            print(a - 1,
                  ':',
                  '\t',
                  b)
        if bool(termin) is False:
            print('Brak terminów do usunięcia.')
            paneladministratora_vhelper()
        for i in range(len(termin)):
            termin_ktory_usunieto = termin.pop(0)
            termin_usunieto.insert(0, termin_ktory_usunieto)
        paneladministratora_vhelper()
    else:
        print('Niepoprawna komenda.')
        paneladministratora_vhelper()


def wyswietlanie_tabele_usuniete_4():
    if bool(termin_usunieto) is False:
        print('Brak terminów do wyświetlenia.')
        paneladministratora_vhelper()
    print('Legenda: ' + '\n' +
          'D - Dzień tygodnia' + '\n' +
          'G - godzina'
          )
    print('\n' + 'Id:',
          '\t',
          '[D: , G: ]',
          )
    numery_termin_pomocniczy = [1 + n for n in range(len(termin_usunieto))]
    numery_termin = {numery_termin_pomocniczy[i]: termin_usunieto[i] for i in range(len(termin_usunieto))}
    for a, b in numery_termin.items():
        print(a - 1,
              ':',
              '\t',
              b)
    paneladministratora_vhelper()


def drukowanie_tabele_usuniete_5():
    if bool(termin_usunieto) is False:
        print('Brak terminów do wydrukowania do pliku.')
        paneladministratora_vhelper()
    if bool(termin_usunieto) is True:
        teraz = datetime.now()
        print('Usunięte tabele wydrukowano do pliku usuniete_tabele.txt')
        numery_termin_usunieto_pomocniczy = [1 + n for n in range(len(termin_usunieto))]
        numery_termin_usunieto = {numery_termin_usunieto_pomocniczy[i]: termin_usunieto[i]
                                  for i in range(len(termin_usunieto))}
        outfile = open('usuniete_tabele.txt', 'a')
        outfile.write('\n' + '- - - - - - - - Nowy wydruk danych - - - - - - - -')
        for a, b in numery_termin_usunieto.items():
            outfile.write('\n' + str(teraz) + '\t' + str(a) + ':' + '\t' + str(b))
        outfile.close()
    paneladministratora_vhelper()


def wyswietlanie_terminu_6():
    print('Legenda: ' + '\n' +
          'Nr - numer pracownika' + '\n' +
          'M - miesiąc' + '\n' +
          'D - dzień' + '\n' +
          'S - start zmiany' + '\n' +
          'K - koniec zmiany'
          )
    print('\n' + 'Id:',
          '\t',
          '[[Nr: ],',
          '[M: , D: ],',
          '[S:, K:]]')
    numery_termin_pomocniczy = [1 + n for n in range(len(termin_pracy))]
    numery_termin = {numery_termin_pomocniczy[i]: termin_pracy[i] for i in range(len(termin_pracy))}
    for a, b in numery_termin.items():
        print(a - 1,
              ':',
              '\t',
              b)
    if bool(termin_pracy) is False:
        print('Brak terminów do wyświetlenia.')
        paneladministratora_vhelper()
    paneladministratora_vhelper()


def usuwanie_terminu_7():
    print('\n' + 'Legenda: ' + '\n' +
          'Nr - numer pracownika' + '\n' +
          'M - miesiąc' + '\n' +
          'D - dzień' + '\n' +
          'S - start zmiany' + '\n' +
          'K - koniec zmiany'
          )
    print('\n' + 'Rozpoczynam usuwanie.')
    print('\n' + 'Id:',
          '\t',
          '[[Nr: ],',
          '[M: , D: ],',
          '[S:, K:]]')
    numery_wejsc_pomocniczy = [1 + n for n in range(len(termin_pracy))]
    numery_wejsc = {numery_wejsc_pomocniczy[i]: termin_pracy[i] for i in range(len(termin_pracy))}
    for a, b in numery_wejsc.items():
        print(a - 1,
              ':',
              '\t',
              b)
    if bool(termin_pracy) is False:
        print('Brak terminów do usunięcia.')
        usuwanie_terminu_menu()
    usun = input('\n' + 'Wybierz numer (Id:) do usunięcia: ')
    if usun.isdigit() and int(usun) >= 0:
        if int(usun) <= len(termin_pracy) - 1:
            usun_int = int(usun)
            termin_ktory_usunieto = termin_pracy.pop(usun_int)
            print('Termin który usunięto: ', termin_ktory_usunieto)
            termin_usunieto_pracowniczy.insert(0, termin_ktory_usunieto)
            print('\n' + 'Legenda: ' + '\n' +
                  'Nr - numer pracownika' + '\n' +
                  'M - miesiąc' + '\n' +
                  'D - dzień' + '\n' +
                  'S - start zmiany' + '\n' +
                  'K - koniec zmiany'
                  )
            print('Histora usuniętych terminów: ')
            print('\n' + 'Id:',
                  '\t',
                  '[[Nr: ],',
                  '[M: , D: ],',
                  '[S:, K:]]')
            numery_wejsc_usunietych_pomocniczy = [1 + n for n in range(len(termin_usunieto_pracowniczy))]
            numery_wejsc_usunietych = {numery_wejsc_usunietych_pomocniczy[i]: termin_usunieto_pracowniczy[i]
                                       for i in range(len(termin_usunieto_pracowniczy))}
            for a, b in numery_wejsc_usunietych.items():
                print(a - 1,
                      ':',
                      '\t',
                      b)
            else:
                print('\n' + 'Pozostałe terminy: ')
                print('\n' + 'Id:',
                      '\t',
                      '[[Nr: ],',
                      '[M: , D: ],',
                      '[S:, K:]]')
                numery_wejsc_pomocniczy = [1 + n for n in range(len(termin_pracy))]
                numery_wejsc = {numery_wejsc_pomocniczy[i]: termin_pracy[i] for i in range(len(termin_pracy))}
                for a, b in numery_wejsc.items():
                    print(a - 1,
                          ':',
                          '\t',
                          b)
            usuwanie_terminu_menu()
        else:
            print('Brak terminów, lub podano nieodpowiednią liczbę.')
            usuwanie_terminu_menu()
    else:
        print('Brak terminów, lub podano nieodpowiednią liczbę.')
        usuwanie_terminu_menu()


def usuwanie_terminu_menu():
    powrot = input('\n' + 'Aby usunąć termin wybierz 1.' + '\n' + 'Aby wrócic do panelu administratora wybierz 2.'
                   + '\n')
    if powrot == str('1'):
        usuwanie_terminu_7()
    elif powrot == str('2'):
        paneladministratora()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n')
        usuwanie_terminu_menu()


def czysczenie_terminu_8():
    potwierdzenie_czyszczenie = input('Aby usunąć wszystkie terminy pracy wpisz komendę: "usun".' + '\n' + 'Komenda: ')
    if potwierdzenie_czyszczenie == str('usun'):
        print('Legenda: ' + '\n' +
              'D - Dzień tygodnia' + '\n' +
              'G - godzina'
              )
        print('\n' + 'Termiy które usunięto.')
        print('Id:',
              '\t',
              '[D: , G: ]',
              )
        numery_termin_pomocniczy = [1 + n for n in range(len(termin_pracy))]
        numery_termin = {numery_termin_pomocniczy[i]: termin_pracy[i] for i in range(len(termin_pracy))}
        for a, b in numery_termin.items():
            print(a - 1,
                  ':',
                  '\t',
                  b)
        if bool(termin_pracy) is False:
            print('Brak terminów do usunięcia.')
            paneladministratora_vhelper()
        for i in range(len(termin_pracy)):
            termin_ktory_usunieto = termin_pracy.pop(0)
            termin_usunieto_pracowniczy.insert(0, termin_ktory_usunieto)
        paneladministratora_vhelper()
    else:
        print('Niepoprawna komenda.')
        paneladministratora_vhelper()
    paneladministratora_vhelper()


def wyswitlanie_terminu_usuniete_9():
    if bool(termin_usunieto_pracowniczy) is False:
        print('Brak terminów do wyświetlenia.')
        paneladministratora_vhelper()
    print('Legenda: ' + '\n' +
          'D - Dzień tygodnia' + '\n' +
          'G - godzina'
          )
    print('\n' + 'Id:',
          '\t',
          '[D: , G: ]',
          )
    numery_termin_pomocniczy = [1 + n for n in range(len(termin_usunieto_pracowniczy))]
    numery_termin = {numery_termin_pomocniczy[i]: termin_usunieto_pracowniczy[i]
                     for i in range(len(termin_usunieto_pracowniczy))}
    for a, b in numery_termin.items():
        print(a - 1,
              ':',
              '\t',
              b)
    paneladministratora_vhelper()


def drukowanie_terminu_usuniete_10():
    if bool(termin_usunieto_pracowniczy) is False:
        print('Brak terminów do wydrukowania do pliku.')
        paneladministratora_vhelper()
    if bool(termin_usunieto_pracowniczy) is True:
        teraz = datetime.now()
        print('Usunięte tabele wydrukowano do pliku usuniete_terminy_pracownicze.txt')
        termin_usunieto_pracowniczy_pomocniczy = [1 + n for n in range(len(termin_usunieto_pracowniczy))]
        numery_termin_usunieto = {termin_usunieto_pracowniczy_pomocniczy[i]: termin_usunieto_pracowniczy[i]
                                  for i in range(len(termin_usunieto_pracowniczy))}
        outfile = open('usuniete_terminy_pracownicze.txt', 'a')
        outfile.write('\n' + '- - - - - - - - - - - - Nowy wydruk danych - - - - - - - - - - - - - - -')
        for a, b in numery_termin_usunieto.items():
            outfile.write('\n' + str(teraz) + '\t' + str(a) + ':' + '\t' + str(b))
        outfile.close()
    paneladministratora_vhelper()


def wlacz_mowe_11():
    global p_mowy
    p_mowy = 1
    paneladministratora_vhelper()


def wylacz_mowe_12():
    global p_mowy
    p_mowy = 0
    paneladministratora_vhelper()


def end():
    exit()


start()
