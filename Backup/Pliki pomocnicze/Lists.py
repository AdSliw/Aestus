import sys, os, winsound, PIL.Image, random, webbrowser, time

imie = ''
nazwisko = ''
wybor_zaaw = ''
termin = [['', '']]
poziom_zaaw = []
lista_uzyt = []
lista_pliki = []


def start():
    print('Ladowanie programu, prosze czekac.')
    print('\n' + 'Witaj! Dodzwoniles sie do najlepszej plywalni w miescie.' + '\n')
    intro()


def end():
    exit()

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


def intro():
    wybor = ''
    print(
        '\n' + 'Aby sprawdzic dostepnosc torow wybierz 1.\nAby umowic sie na zejcia z instruktorem wybierz 2.\nAby zarezerwowac tor wybierz 3.\nAby otworzyc grafik wybierz 4.\nAby otworzyc strone internetowa basenu wybierz 5.\nAby otworzyc panel administratora wybierz 6.' + '\n')
    wybor = input('Co chcesz zrobic(1,2,3,4,5,6)?' + '\n' + 'Numer:')
    print('\n' + 'Wybrales numer: ' + wybor + '\n')
    if wybor == str(1):
        print('\n' + 'Chcesz sprawdzic dostepnosc torow.')
        wybor1()
    if wybor == str(2):
        print('\n' + 'Chcesz zamowic zajecia z instruktorem.')
        wybor2()
    if wybor == str(3):
        print('\n' + 'Chcesz zarezerowac tor.')
        wybor3()
    if wybor == str(4):
        print('\n' + 'Chcesz otworzyc grafik.')
        #grafik()
    if wybor == str(5):
        print('\n' + 'Chcesz otworzyc strone internetowa basenu.')
        #stronainternetowa()
    if wybor == str(6):
        print('\n' + 'Otwieranie panelu administratora.')
        paneladministratora()
    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        intro()


def wybor1():
    zajety = 0
    dzien = ''
    godzina = ''
    print('\n' + 'Na jaki dzien sprawdzic dostepnosc?')
    dzien = input('\n' + 'Podaj numer dnia(gdzie poniedzialek = 1, niedziela = 7): ' + '\n')
    godzina = input('\n' + 'Podaj godzine (tylko pelne godziny do 6 do 20 godziny): ' + '\n')
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
                    print(
                        '\n' + 'Aby zarezerwowac tor wybierz 1' + '\n' + 'Aby zamowic zajecia z instruktorem wybierz 2' + '\n' + 'Aby wrocic do menu glownego wybierz 3.' + '\n')
                    wybor_inna_opcja = input()
                    if wybor_inna_opcja == str(1):
                        wybor3()
                    if wybor_inna_opcja == str(2):
                        wybor2()
                    if wybor_inna_opcja == str(3):
                        intro()
            else:
                print(
                    '\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                wybor_inny_termin = input()
                if wybor_inny_termin == str(1):
                    wybor1()
                if wybor_inny_termin == str(2):
                    intro()

    else:
        print('Potrzebna liczba!' + '\n')
        wybor1()


def wybor2():
    print(
        '\n' + 'Wybierz poziom zaawansowania:' + '\n' + 'Poczatkujacy(1)' + '\n' + 'Sredniozaawansowany(2)' + '\n' + 'Zaawansowany(3)' + '\n')
    wybor_zaaw = input()
    if wybor_zaaw == str(1):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom poczatkujacy')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3()

    if wybor_zaaw == str(2):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom sredniozaawansowany')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3()

    if wybor_zaaw == str(3):
        print('\n' + 'Wybrano: ' + wybor_zaaw + ' - poziom zaawansowany')
        poziom_zaaw.append(wybor_zaaw)
        # print(poziom_zaaw)
        wybor3()

    else:
        print('\n' + 'Prosze wybrac odpowiednia liczbe!' + '\n' + '\n')
        wybor2()


def wybor3():
    lista_uzyt = []
    imie = input('Aby rozpoczac rezerwacje, wpisz swoje imie' + '\n')
    nazwisko = input('I nazwisko:' + '\n')
    zajety = 0
    print('\n' + 'Na jaki dzien zarezerwowac tor?')
    dzien = input('\n' + 'Podaj numer dnia(gdzie poniedzialek = 1, niedziela = 7): ' + '\n')
    godzina = input('\n' + 'Podaj godzine (tylko pelne godziny do 6 do 20 godziny): ' + '\n')
    if dzien.isdigit():
        if godzina.isdigit():
            if int(godzina) < 21 and int(godzina) > 5 and int(dzien) > 0 and int(dzien) < 8:
                for element in termin:
                    if element[0] == str(dzien):
                        if element[1] == str(godzina):
                            zajety = 1
                            print(
                                '\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                            wybor_inny_termin = input()
                            if wybor_inny_termin == str(1):
                                wybor3()
                            if wybor_inny_termin == str(2):
                                intro()
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
                    # ^^^fajnie byloby wrzucic tutaj odmiane z NLTK
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
                    intro()
            else:
                print(
                    '\n' + 'Termin niedostepny. Aby wybrac inny termin wybierz 1, aby wrocic do menu glownego wybierz 2.' + '\n')
                wybor_inny_termin = input()
                if wybor_inny_termin == str(1):
                    wybor3()
                if wybor_inny_termin == str(2):
                    intro()
    else:
        print('Potrzebna liczba!' + '\n')
        wybor3()


start()






