#import time

termin_pracy = [[['  '], [' ', ' '], [' ', '  ']],
                [['11'], ['12', '31'], ['8', '16']], [['72'], ['1', '1'], ['16', '20']]]
termin_pracy_pomocniczy = []
numer_pracownika = []
lista_pomocnicza_godzin = []
lista_pomocnicza_dni = []
lista_pomocnicza_numeru_pracownika = []
termin_usunieto_pracowniczy = []
termin_usunieto_uzytkownika = []


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
    usun = input ('\n' + 'Wybierz numer (Id:) do usunięcia: ')
    if usun.isdigit() and int(usun) >=0:
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
            numery_wejsc_usunietych = {numery_wejsc_usunietych_pomocniczy[i]: termin_usunieto_pracowniczy[i] for i in range(
                len(termin_usunieto_pracowniczy))}
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


panelpracownika()
