import json
termin = [['', '']]
lista_uzyt = []
termin_2 = []
termin_usunieto = []
#def clearspecific():
#    print(termin)
#    clear_choice = input('Wybierz dzień:')
#    if element[0] in termin

#def clearspecific_v2():
#    clear_choice_v2 = input('Wybierz dzien:')
#    for element in termin:
#        if any(element) == clear_choice_v2:
#            if element[1] == str(godzina):

def dodaj():
    lista_uzyt = []
    dzien = input('\n' + 'Podaj numer dnia:')
    godzina = input('\n' + 'Podaj godzine:')
    lista_uzyt.append(dzien)
    lista_uzyt.append(godzina)
    termin.append(lista_uzyt)
    dalej = input('dalej?(t/n)')
    if dalej == str('t'):
        dodaj()
    else:
        usun()


def dalej2():
    dalej2 = input('usunac?(t/n)')
    if dalej2 == str('t'):
        usun()
    else:
        print('koniec')
        
def usun():
    termin_2 = [(idx, item) for idx,item in enumerate(termin)]
    print(termin_2)
    usun = input ('wybierz numer do usuniecia')
    usun_int = int(usun)
    termin_ktory_usunieto = termin_2.pop(usun_int)
    print('termin ktory usunieto: ',termin_ktory_usunieto)
    del termin[usun_int]
    termin_2 = [(idx, item) for idx,item in enumerate(termin)]
    print(termin_2, sep = '\n')
    print(termin)
    numery_wejsc = [1 + n for n in range(len(termin))]
    res = {numery_wejsc[i]: termin[i] for i in range(len(termin))}    
    for a, b in res.items():
        print(a - 1, ':', b) 
    dalej2()

    #for a, b in termin:
        #print(a, b)
        #if a == str('1'):
            #print('poniedzialek', 'godzina: ', b)
        #else:
            #print('blad')
    
        #doom = [str('poniedzialek') if x == 1 else x for x in termin]
    
        #for element in termin:
            #if element[0] in termin == poniedzialek:
            #    print('ok')
            #else:
            #    print('nieok')
    #for a in termin:
    #    print(index, a)
    #    index += 1

  

#            print('ok')
#        elif a == 2:
#            print('wtorek', b)
#        elif a == 3:
#            print('sroda', b)
#        elif a == 4:
#            print('czwartek', b)            
#        elif a == 5:
#            print('piatek', b)
#        elif a == 6:
#            print('sobota', b)
#        elif a == 7:
#            print('niedziela', b)

    #lul = [str('poniedzialek') if x[1] in res == '1' else a for a in res]
    #print(lul)
        

    

#termin_enumerated = list(enumerate(termin))
#print(termin_enumerated)    

#def clear():
    #x = int(input('wybierz numer dnia: '))
    #print(termin)
    #for a in termin[0]:
    #    termin.append('key:')
    #print(termin)
    
    #for element in termin_enumerated:
        #if termin_enumerated[0]==x:
            #print("wybrano {}".format(termin_enumerated[x]))
        #else:
    #clear()
        #class_ = type(x)
        #class_element = element[0]
        #print(class_)
        #print(class_element)
        #if element[0] != x:
            #del termin_enumerated[x]
            #print(termin_enumerated)
        
        #clear()

    #result = filter(lambda val: val !=  x, termin)
    #print(list(result))
    #myList = [value for value in termin if value != x]
    #print(myList)
#    try:    
#        while True:
#            termin.remove(x)
#            print(termin)
#    except ValueError:
#        print('fail')
#        print(termin)
#        pass


def panelpracownika():
    print('\n' + 'Witaj pracowniku.')
    print('Aby wyświetlić listę zmian wybierz 1.\nAby dodać swoją zmianę wybierz 2.\nAby _ 3.\nAby wrocic do menu wybierz glownego 4.\n')
    wyborpracownik = ''
    wyborpracownik = input('Co chcesz zrobic(1,2,3)?' + '\n' + 'Numer:')
    if wyboradmin == str(1):
        print('\n' + 'Oto lista przypisanych zmian:' + '\n')
        #print(termin)
        drukowanie_termin_pracy()
    elif wyborpracownik == str(2):
        print('\n' + 'Rozpoczynam proces dodawania zmiany.' + '\n')
        time.sleep(1)
        godziny_wejscia_i_wyjscia()
    elif wyborpracownik == str(3):
        print('\n' + '_' + '\n')
        time.sleep(1)
        _()
    elif wyborpracownik == str(4):
        print('\n' + 'Wracam do menu.' + '\n')
        time.sleep(1)
        intro()
    else:
        print('\n' + 'Prosze wybrac odpowiednią liczbe!' + '\n' + '\n')
        paneladministratora()

dodaj()




