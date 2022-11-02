#Napiš funkci 'vyhodnot', která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec
#podle stavu hry:
#"x" – Vyhrál hráč s křížky (pole obsahuje xxx)
#"o" – Vyhrál hráč s kolečky (pole obsahuje ooo)
#"!" – Remíza (pole neobsahuje -, a nikdo nevyhrál)
#"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

def vyhodnot(my_field):
    '''Vyhodnoti herni pole podle stavu hry.'''    
    if 'xxx' in my_field:
        print('Vyhral jsi!')
        return 'x'
    elif 'ooo' in my_field:
        print('Prohral jsi!')
        return 'o'
    elif '-' not in my_field:
        print('Remiza!')
        return '!'
    else: 
        return '-'
       


