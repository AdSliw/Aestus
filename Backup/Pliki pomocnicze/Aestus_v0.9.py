import winsound, PIL.Image, random, webbrowser, time
import speech_recognition as sr
import pyttsx3 as tts


#TODO Spytać o:
# do kiedy praca,
# jaka czcionka, interlinia etc
# czy przy tak długim kodzie rozpisywać się o schemat blokowy, nagrywanie, praata, etc


#TODO ZROBIĆ BACKUP !


#TODO Przygotować ankietę!


#TODO posprawdzać pisownie printów i mow'ów
#TODO dodać informacje o nie używaniu polskich znaków
#TODO dodać czyszczenie poszczególnych dni
#TODO dodać instrukcje

#TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#TODO dokonczyć panel administratora
    #TODO dodać przełącznik mowy w panelu admina
    #TODO przenieść usuwanie terminów pracy do admina
#TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

r = sr.Recognizer()
engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
p_mowy = 1


def mow(text):
    if p_mowy == 1:
        engine.say(text)
        engine.runAndWait()
    if p_mowy == 0:
        pass


termin_pracy = [[['  '], [' ', ' '], [' ', '  ']]]
termin_pracy_pomocniczy = []
numer_pracownika = []
lista_pomocnicza_godzin = []
lista_pomocnicza_dni = []
lista_pomocnicza_numeru_pracownika = []
termin_usunieto_pracowniczy = []
termin_usunieto_uzytkownika = []
wybor_zaaw = ''
termin = [['', '']]
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


def start():
    print('Ładowanie programu, proszę czekać.')
    mow('ładowanie programu, proszę czekać.')
    for x in range(0, 3):
        b = "." * x
        print(b, end="\r")
    time.sleep(1)
    print('\n' + 'Witaj! Dodzwoniłeś się do najlepszej pływalni w mieście.' + '\n')
    mow('Witaj! Dodzwoniłeś się do najlepszej pływalni w mieście.')
    winsound.PlaySound('WAV/basen.wav', winsound.SND_ASYNC)
    intro()

#todo instrukcja


def instrukcja():
    print('Oto krótka instrukcja, uzywaj głosowych zwrotów takich jak, '
          'jeden, dwa, trzy, aby wybierać poszczególne opcje z menu.')
    mow('Oto krótka instrukcja, uzywaj głosowych zwrotów takich jak, '
        'jeden, dwa, trzy, aby wybierać poszczególne opcje z menu.')


def intro():
    print('\n' + 'Aby sprawdzić dostępność torów powiedz 1.'
                 '\nAby zamówić zajęcia z instruktorem powiedz 2.'
                 '\nAby zarezerwować tor powiedz 3.'
                 '\nAby otworzyć grafik powiedz 4.'
                 '\nAby otworzyć stronę internetową basenu powiedz 5.'
                 '\nAby otworzyć panel pracowniczy powiedz 6.' + '\n')

    mow('Aby sprawdzić dostępność torów powiedz jeden.')
    mow('Aby zamówić zajęcia z instruktorem powiedz dwa.')
    mow('Aby zarezerwować tor powiedz trzy.')
    mow('Aby otworzyć grafik powiedz cztery.')
    mow('Aby otworzyć stronę internetową basenu powiedz pięć.')
    mow('Aby otworzyć panel pracownika powiedz sześć')

    print('Co chcesz zrobic(1,2,3,4,5,6)?' + '\n' + 'Numer:')
    print('Slucham...')
    mow('Słucham')
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
        else:
            intro_1()
        print('\n' + 'Wybrano numer: ' + wybor + '\n')
        mow('Wybrano numer: ' + wybor)
        if wybor == str(1):
            print('\n' + 'Chcesz sprawdzic dostepnosc torow.')
            mow('Chcesz sprawdzić dostępność torów.')
            wybor1DzienPrinty()
        if wybor == str(2):
            print('\n' + 'Chcesz zamowic zajecia z instruktorem.')
            mow('Chcesz zamowić zajęcia z instruktorem.')
            wybor2Printy()
        if wybor == str(3):
            print('\n' + 'Chcesz zarezerowac tor.')
            mow('Chcesz zarezerwować tor.')
            wybor3Printy()
        if wybor == str(4):
            print('\n' + 'Chcesz otworzyc grafik.')
            mow('Chcesz otworzyć grafik.')
            grafik()
        if wybor == str(5):
            print('\n' + 'Chcesz otworzyc strone internetowa basenu.')
            mow('Chcesz otworzyć stronę internetową basenu.')
            stronainternetowa()
        if wybor == str(6):
            print('\n' + 'Otwieranie panelu pracowniczego.')
            mow('Otwieranie panelu pracowniczego.')
            haslo()
        else:
            print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
            mow('Proszę wybrać odpowiednią liczbę.')
            intro()


#todo przeniesc usuwanie terminow pracy do admina


def panelpracownika():
    pp = input('\n' + 'Wybierz 1 aby dodać godziny wejscia i wyjscia, ' + '\n' +
                      'Wybierz 2 aby wyświetlić aktualne terminy pracy, ' + '\n' +
                      'Wybierz 3 aby rozpocząć usuwanie terminów pracy, ' + '\n' +
                      'Wybierz 4 aby wyświetlić historię usuniętych terminów pracy.' + '\n' +
                      'Wybierz 5 aby wrócić do głównego menu.' + '\n' + 'Wybór: ')
    if pp == str('1'):
        godziny_wejscia_i_wyjscia()
    elif pp == str('2'):
        drukowanie_termin_pracy()
    elif pp == str('3'):
        usuwanie_terminu_pracowniczy()
    elif pp == str('4'):
        drukowanie_historii_usuwania()
    elif pp == str('5'):
        intro()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
        panelpracownika()


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
    print('N:', '\t', '\t', termin_pracy_pomocniczy)
    sprawdzenie_danych = input('\n' + 'Sprawdź poprawnośc danych.' + '\n' + 'Jeśli dane są poprawne wybierz 1. ' +
                               '\n' + 'Aby porawić dane wybierz 2. ' + '\n' + 'Wybór: ')
    if sprawdzenie_danych == str('1'):
        termin_pracy.append(termin_pracy_pomocniczy)
        godziny_wejscia_i_wyjscia_menu()
    elif sprawdzenie_danych == str('2'):
        godziny_wejscia_i_wyjscia()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n' + '\n')
        usuwanie_terminu_pracowniczy_menu()


def drukowanie_termin_pracy():
    print('\n' + 'Wyświetlanie terminów pracy:')
    if bool(termin_pracy) is False:
        print('Brak terminów do wyświetlenia.')
        usuwanie_terminu_pracowniczy_menu()
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
    panelpracownika()

#to usunac z panelu pracownika//przeniesiono do panelu administratora
def usuwanie_terminu_pracowniczy_menu():
    powrot = input('\n' + 'Aby usunąć termin wybierz 1.' + '\n' + 'Aby wrócic do panelu pracownika wybierz 2.' + '\n')
    if powrot == str('1'):
        usuwanie_terminu_pracowniczy()
    elif powrot == str('2'):
        panelpracownika()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n')
        usuwanie_terminu_pracowniczy_menu()


def usuwanie_terminu_pracowniczy():
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
        usuwanie_terminu_pracowniczy_menu()
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
            usuwanie_terminu_pracowniczy_menu()
        else:
            print('Brak terminów, lub podano nieodpowiednią liczbę.')
            usuwanie_terminu_pracowniczy_menu()
    else:
        print('Brak terminów, lub podano nieodpowiednią liczbę.')
        usuwanie_terminu_pracowniczy_menu()

#TODO zmienić na inną nazwę eg: wyswietlanie_historii_usuwania_terminy
def drukowanie_historii_usuwania():
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
    panelpracownika()


def wybor1DzienPrinty():
    print('\n' + 'Na jaki dzien sprawdzic dostepnosc?')
    mow('Na jaki dzień sprawdzić dostępność')
    print('\n' + 'Podaj dzień: ' + '\n')
    mow('Podaj dzień')
    print('Słucham...')
    mow('Słucham')
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
        else:
            wybor1Dzien()
    #print(dzien)
    if dzien == str(1):
        print('Wybrano podziedziałek.')
        mow('Wybrano podziedziałek.')
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
        print('Wybrano sobota.')
        mow('Wybrano sobota.')
    elif dzien == str(7):
        print('Wybrano niedzielę.')
        mow('Wybrano niedzielę.')
    else:
        wybor1Dzien()
    wybor1GodzinaPrinty()


def wybor1GodzinaPrinty():
    print('\n' + 'Podaj godzine (tylko pelne godziny od 6 do 20 godziny): ' + '\n')
    mow('Podaj godzinę.')
    print('Słucham...')
    mow('Słucham')
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
                            mow('Tor w tym terminie jest zajety.')
                            zajety = 1
                            intro()
                if zajety == 0:
                    print('\n' + 'Tory o tej godzine sa dostepne.' + '\n')
                    mow('Tory o tej godzine sa dostepne.')
                    print('\n' + 'Aby zarezerwowac tor powiedz 1' + '\n' +
                          'Aby zamowic zajecia z instruktorem powiedz 2' + '\n' +
                          'Aby wrocic do menu glownego powiedz 3.' + '\n')
                    mow('Aby zarezerwowac tor powiedz 1.')
                    mow('Aby zamowic zajecia z instruktorem powiedz 2.')
                    mow('Aby wrocic do menu glownego powiedz 3.')
                    print('Słucham...')
                    wybor1_2()
            else:
                print('\n' + 'Termin niedostepny. Aby wybrac inny termin powiedz 1, '
                             'aby wrocic do menu glownego powiedz 2.' + '\n')
                mow('Termin niedostępny. Aby wybrac inny termin powiedz 1, aby wrócic do menu głównego wybierz 2.')
                wybor1_3()
    else:
        print('Potrzebna liczba!' + '\n')
        mow('Potrzebna liczba')
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
    if wybor_inna_opcja == str(1):
        wybor1()
    if wybor_inna_opcja == str(2):
        intro()


def wybor2Printy():
    print('\n' + 'Wybierz poziom zaawansowania:' + '\n' +
          'Poczatkujacy(1)' + '\n' +
          'Sredniozaawansowany(2)' + '\n' +
          'Zaawansowany(3)' + '\n')
    mow('Wybierz poziom zaawansowania, aby wybrać poziom początkujący powiedz jeden, '
        'aby wybrać poziom średniozaawansowany powiedz dwa, '
        'aby wybrać poziom zaawansowany powiedz trzy,')
    print('Słucham...')
    mow('Słucham')
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


def wybor3Printy():
    print('Otiweram rezerwację toru.')
    mow('Otwieram rezerwację toru.')
    wybor3DzienPrinty()


def wybor3DzienPrinty():
    print('\n' + 'Na jaki dzien zarezerwowac tor?')
    mow('Na jaki dzień zarezerwować tor?')
    print('\n' + 'Podaj dzień: ' + '\n')
    mow('Podaj dzień.')
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
        print('Wybrano sobota.')
        mow('Wybrano sobota.')
    elif dzien == str(7):
        print('Wybrano niedzielę.')
        mow('Wybrano niedzielę.')
    else:
        wybor3Dzien()
    #print(dzien)
    wybor3GodzinaPrinty()


def wybor3GodzinaPrinty():
    print('\n' + 'Podaj godzinę (tylko pelne godziny od 6 do 20 godziny): ' + '\n')
    mow('Podaj godzinę, obowiązują tylko pełne godziny od szóstej do dwudziestej. ')
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
    #print(dzien)
    #print(godzina)
    wybor3()


def wybor3():
    lista_uzyt = []
    imie = ''
    nazwisko = ''
    print('Aby rozpoczac rezerwacje, wpisz najpierw swoje imie i wcisnij enter:' + '\n')
    mow('Aby rozpocząć rezerwację, wpisz najpierw swoie imię i wciśnij enter.')
    imie = input('Imię: ')
    print('Teraz wpisz swoje nazwisko i wcisnij enter:' + '\n')
    mow('Teraz wpisz swoje nazwisko i wciśnij enter.')
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
    nazwisko_bezpz = ''.join(nazwisko_lista)
    zajety = 0
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin:
                    if element[0] == str(dzien):
                        if element[1] == str(godzina):
                            zajety = 1
                            print('\n' + 'Termin niedostępny. Aby wybrać inny termin powiedz jeden, '
                                         'aby wrocic do menu głównego powiedz dwa.' + '\n')
                            mow('termin niedostępny, aby wybrać inny termin powiedz jeden,'
                                'aby wrócić do menu głównego powiedz dwa')
                            wybor3_1()
                if zajety == 0:
                    lista_uzyt.append(dzien)
                    # print(lista_uzyt)
                    lista_uzyt.append(godzina)
                    # print(lista_uzyt)
                    termin.append(lista_uzyt)
                    # print(termin)
                    outfile = open('dane.txt', 'a')
                    outfile.write(dzien + '\t' + godzina + '\t' + imie_bezpz + '\t'
                                  + nazwisko_bezpz + '\t' + str(poziom_zaaw) + '\n')
                    outfile.close()
                    # print(str(poziom_zaaw))
                    print('\n' + 'Dziękujemy za skorzystanie z usługi użytkowniku' + ' ' + imie + ' ' + nazwisko + '!')
                    mow('Dziękujemy za skorzystanie z usługi użytkowniku' + ' ' + imie + ' ' + nazwisko + '!')
                    print('\n' + 'Wybrano następujace dni i godziny [i poziom zaawansowania]:')
                    mow('Wybrano następujace dni i godziny')
                    if dzien == str(1):
                        print('Poniedziałek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Poniedziałek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(2):
                        print('Wtorek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Wtorek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(3):
                        print('Środa godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Środa godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(4):
                        print('Czwartek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Czwartek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(5):
                        print('Piątek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Piątek godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(6):
                        print('Sobota godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Sobota godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    if dzien == str(7):
                        print('Niedziela godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                        mow('Niedziela godzina:' + ' ' + godzina + ' ' + str(poziom_zaaw))
                    list.clear(poziom_zaaw)
                    dziekiPrinty()
            else:
                print('\n' + 'Termin niedostępny. Aby wybrać inny termin powiedz jeden, '
                             'aby wrócić do menu głównego powiedz dwa.' + '\n')
                mow('Termin niedostępny. Aby wybrać inny termin powiedz jeden, '
                    'aby wrócić do menu głównego powiedz dwa.')
                wybor3_2()
    else:
        print('Potrzebna liczba!' + '\n')
        mow('Potrzebna liczba!')
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


def wybor3_2():
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            wybor3_2()
        if wybor_audio == 'jeden':
            wybor_inna_opcja_4 = str(1)
        elif wybor_audio == '1':
            wybor_inna_opcja_4 = str(1)
        elif wybor_audio == '2':
            wybor_inna_opcja_4 = str(2)
        else:
            wybor3()
    if wybor_inna_opcja_4 == str(1):
        wybor3Printy()
    if wybor_inna_opcja_4 == str(2):
        intro()


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
    print('\nAby wrócić do menu głównego powiedz 1.\nAby wyświetlić motywującą wiadmość powiedz 2.' + '\n')
    mow('Aby wrócić do menu głównego powiedz jeden.')
    mow('Aby wyświetlić motywującą wiadmość powiedz dwa.')
    print('Co chcesz zrobic(1,2)?' + '\n')
    mow('Co chcesz zrobić? Słucham')
    dzieki()


def dzieki():
    wybor_inna_opcja_5 = ''
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=3)
            wybor_audio = r.recognize_google(audio, language='pl-PL')
        except:
            print(end='.')
            dzieki()
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
        # print('Ladowanie programu, prosze czekac.')
        # for x in range (0,3):
        # b = "." * x
        # print (b, end="\r")
        # time.sleep(1)
        intro()
    if wybor_inna_opcja_5 == str(2):
        print('\n' + 'Wybrałeś numer: ' + wybor_inna_opcja_5 + '\n')
        mow('Wybrałeś numer: ' + wybor_inna_opcja_5)
        plik = open('TEXT/motywacja.txt')
        motywacja = plik.readlines()
        plik.close()
        losowe = random.choice(motywacja)
        dawaj = losowe.strip()
        print(dawaj)
        mow(dawaj)
        dziekiPrinty()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        mow('Proszę wybrać odpowiednią liczbę!')
        dziekiPrinty()


def haslo():
    haslo_admin = 'aestusa'
    haslo_pracownik = 'aestusp'
    #print('Prosze czekac.')
    #for x in range(0, 3):
    #    b = "." * x
    #    print(b, end="\r")
    time.sleep(1)
    print('\n' + 'Podaj haslo:' + '\n')
    podanehaslo = input()
    if podanehaslo == haslo_admin:
        print('Sprawdzanie hasla.')
        for x in range(0, 3):
            b = "." * x
            print(b, end="\r")
            time.sleep(1)
        paneladministratora()
    if podanehaslo == haslo_pracownik:
        print('Sprawdzanie hasla.')
        for x in range(0, 3):
            b = "." * x
            print(b, end="\r")
            time.sleep(1)
        panelpracownika()
    else:
        print('Niepoprawne haslo!')
        intro()


def paneladministratora():
    print('\n' + 'Witaj administratorze.')
    print('1 - aby wyswietlic tabele.'
          '\n2 - aby rozpocząć usuwanie tabel.'
          '\n3 - aby usunąć wszystkie tabele.' #tutaj_przeniesc_do_usunietej tabeli 
          '\n4 - aby wyświetlić usunięte tabele.'
          '\n5 - aby wydrukować historię usuniętych tabel do pliku zewnętrznego.'
          ###
          '\n6 - aby wyświetlić aktualne terminy pracy.'
          '\n7 - aby rozpocząć usuwanie terminów pracy.'
          '\n8 - aby usunąć wszystkie tabele.' #tutaj_przeniesc_do_usunietej tabeli
          '\n9 - aby wyświetlić historię usuniętych terminów pracy.'
          '\n10 - aby wydrukować historię usuniętych terminów pracy do pliku zewnętrznego.'
          ###
          '\n11 - aby włączyć mowę.'
          '\n12 - aby wyłączyć mowe.'
          '\n13 - aby zakonczyc program.'
          '\n14 - aby wrocic do menu glownego.\n')
    wyboradmin = ''
    wyboradmin = input('Co chcesz zrobic(1,2,3)?' + '\n' + 'Numer:')
    if wyboradmin == str(1):
        print('\n' + 'Tabele:' + '\n')
        print(termin)
        paneladministratora()
    elif wyboradmin == str(2):
        print('\n' + 'Rozpoczynam usuwanie tabel.' + '\n')
        usuwanie_terminu()
    elif wyboradmin == str(3):
        print('\n' + 'Rozpoczynam usuwanie wszystkich tabel.' + '\n')
        czyszczeniewszystkichtabel()#TODO tutaj przenoszenie do listy usunietych
    elif wyboradmin == str(4):
        print('\n' + 'Wyświetlam usunięte tabele.' + '\n')
        wyswietlanie_terminu()
    elif wyboradmin == str(5):
        print('\n' + 'Drukuje historię usuniętych tabel do pliku zewnętrznego' + '\n')
        usuwanie_terminu_pracowniczy()
    elif wyboradmin == str(6):
        print('\n' + 'Wyświetlam aktualne terminy pracy' + '\n')
        #()
    elif wyboradmin == str(7):
        print('\n' + 'Rozpoczynam usuwanie terminów pracy. ' + '\n')
        #()
    elif wyboradmin == str(8):
        print('\n' + 'Rozpoczynam usuwanie terminów pracy.' + '\n')
        #()
    elif wyboradmin == str(9):
        print('\n' + 'Drukuje historię usuniętych terminów pracy do pliku zewnętrznego.' + '\n')
        #()
    elif wyboradmin == str(10):
        print('\n' + 'Drukuje historię usuniętych terminów pracy do pliku zewnętrznego.' + '\n')
        drukowanie_historii_usuwania()
    elif wyboradmin == str(11):
        print('\n' + 'Mowa wyłączona.' + '\n')
        #()
    elif wyboradmin == str(12):
        print('\n' + 'Mowa wyłączona.' + '\n')
        #()
    elif wyboradmin == str(13):
        print('\n' + 'Koncze program.' + '\n')
        end()
    elif wyboradmin == str(14):
        print('\n' + 'Wracam do menu.' + '\n')
        intro()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        paneladministratora()


start()
