#Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a
#tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
#Nezapomeň kontrolovat stav hry po každém tahu.

from curses.ascii import isdigit
from random import randrange


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

def tah(field, position, symbol):
    '''Vrati herni pole s danym symbolem umistenym na danou pozici.'''
    start = field[:position]
    end = field[position + 1:]
    if (position >= 0 and position <= 19 and 
        symbol == 'x' or symbol == 'o'):
        change = start + symbol + end 
        return change    
    else:
        return False   

def tah_hrace(field):
    '''Vrati herni pole se zaznamenanym tahem hrace.'''
    while True:
        player_position = input('Zadej cislo pozice: ')
        if player_position.isdigit():
            break
        print('Spatne zadana pozice.')

    while True:
        player_position = int(player_position)    
        if (player_position >= 0 and player_position <= 19 and 
           field[player_position] == '-'):
           return tah(field, player_position, 'x' )    
        print('Spatne zadana pozice.')
        player_position = input('Zadej cislo pozice: ')

def tah_pocitace(field):
    '''Vrati herni pole se zaznamenanym tahem pocitace.'''
    while True:
        pc_position = randrange(20)
        if field[pc_position] == '-':
            return tah(field, pc_position, 'o')   

def piskvorky1d(): 
    '''Hra piskvorky 1D'''
    game_field = (20 * '-')
    print('0.kolo:', game_field)
    print('Tvuj symbole je: x')
    r = 0
    for i in range(1,21):
        x_game_field = tah_hrace(game_field)
        r += 1
        print(r, '.kolo:', x_game_field)        
        if vyhodnot(x_game_field) != '-':
            break
        else:
            r += 1    
            o_game_field = tah_pocitace(x_game_field)
            print(r, '.kolo:', o_game_field)            
            if vyhodnot(o_game_field) != '-':
                break       
            elif o_game_field:
                game_field = o_game_field
    return                 

        


piskvorky1d()   
    
