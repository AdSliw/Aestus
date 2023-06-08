from datetime import datetime

termin = [['', ''], ['0', '3'], ['2', '1']]
termin_usunieto = []
termin_pracy = [[['  '], [' ', ' '], [' ', ' ']],[['2'], ['2', '2'], ['2', '2']],
                      [['11'], ['11', '11'], ['11', '11']]]
termin_usunieto_pracowniczy = []

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

def paneladministratora_vhelper():
    input('\n' + 'Wciśnij enter aby wyświetlić panel administratora.' + '\n')
    paneladministratora()


def paneladministratora():
    print('\n' + 'Witaj administratorze.')
    print('\n' + 'Wybierz:')
    print('1 - aby wyswietlic tabele.'
          '\n2 - aby rozpocząć usuwanie tabel.'
          '\n3 - aby usunąć wszystkie tabele.' #tutaj_przeniesc_do_usunietej tabeli 
          '\n4 - aby wyświetlić usunięte tabele.'
          '\n5 - aby wydrukować historię usuniętych tabel do pliku zewnętrznego.'
          ###
          '\n6 - aby wyświetlić aktualne terminy pracy.'
          '\n7 - aby rozpocząć usuwanie terminów pracy.'
          '\n8 - aby usunąć wszystkie terminy pracy.' #tutaj_przeniesc_do_usunietej tabeli
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
        wyswietlanie_tabele_1() #DONE
    elif wyboradmin == str(2):
        print('\n' + 'Rozpoczynam usuwanie tabel.' + '\n')
        usuwanie_tabele_2() #DONE
    elif wyboradmin == str(3):
        print('\n' + 'Rozpoczynam usuwanie wszystkich tabel.' + '\n')
        czyszczenie_tabele_3()#TODO tutaj przenoszenie do listy usunietych
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
        print('\n' + 'Mowa wyłączona.' + '\n')
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
    potwierdzenie = input('Aby usunąć wszystkie tabele wpisz komendę: "usun".' + '\n' + 'Komenda: ')
    if potwierdzenie == str('usun'):
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
        numery_termin_usunieto = {numery_termin_usunieto_pomocniczy[i]: termin_usunieto[i] for i in range(len(termin_usunieto))}
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
    powrot = input('\n' + 'Aby usunąć termin wybierz 1.' + '\n' + 'Aby wrócic do panelu administratora wybierz 2.' + '\n')
    if powrot == str('1'):
        usuwanie_terminu_7()
    elif powrot == str('2'):
        paneladministratora()
    else:
        print('\n' + 'Proszę wybrać odpowiednią liczbę!' + '\n')
        usuwanie_terminu_menu()


def czysczenie_terminu_8():
    potwierdzenie = input('Aby usunąć wszystkie terminy pracy wpisz komendę: "usun".' + '\n' + 'Komenda: ')
    if potwierdzenie == str('usun'):
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
    numery_termin = {numery_termin_pomocniczy[i]: termin_usunieto_pracowniczy[i] for i in range(len(termin_usunieto_pracowniczy))}
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
    print('Mowa włączona.')
    p_mowy = 1
    paneladministratora_vhelper()


def wylacz_mowe_12():
    print('Mowa włączona.')
    p_mowy = 0
    paneladministratora_vhelper()


def end():
    exit()
