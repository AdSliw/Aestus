def #DEFINICJA():
    #wybor = ''
    with sr.Microphone() as source:
        for i in range(5):
            try:
                print(end='.')
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
                wybor_audio = r.recognize_google(audio, language='pl-PL')
                #print(wybor_audio)
                #######################################################
            except:
                continue
    print('\nNie udało się rozpoznać mowy.'
          '\nWybierz:'
          '\n1  aby spróbować ponownie.'
          '\n2  aby wybrać opcję klawiaturą.\n')

    def wybor_awaryjny():
        wybor_awaryjny_input = input('Co chcesz zrobić?'
                                     '\nWybór: ')
        if wybor_awaryjny_input == str('1'):
            #DEFINICJA()
        elif wybor_awaryjny_input == str('2'):
            #wybor = ''
            wybor_audio = input('Którą opcję wybierasz?\n')
            ################################################
        else:
            print('Proszę wybrać odpowiednią liczbę. ')
            mow('Proszę wybrać odpowiednią liczbę. ')
            wybor_awaryjny()

    wybor_awaryjny()
