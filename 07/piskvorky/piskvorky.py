from util import tah
from ai import tah_pocitace


def tah_hrace(field):
    '''Vrati herni pole se zaznamenanym tahem hrace.'''
    while True:
        player_position = input('Zadej cislo pozice: ')
        if player_position.isdigit():
            break
        print('Spatne zadana pozice.')

    while True:
        player_position = int(player_position)
        if (player_position in range(0, 20) and
                field[player_position] == '-'):
            return tah(field, player_position, 'x')
        print('Spatne zadana pozice.')
        return tah_hrace(field)


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


def piskvorky1d():
    '''Hra piskvorky 1D'''
    game_field = 20 * '-'
    print('0.kolo:', game_field)
    print('Tvuj symbole je: x')
    game_round = 0

    while True:
        x_game_field = tah_hrace(game_field)
        game_round += 1
        print(game_round, '.kolo:', x_game_field)
        if vyhodnot(x_game_field) != '-':
            break
        else:
            game_round += 1
            o_game_field = tah_pocitace(x_game_field)
            print(game_round, '.kolo:', o_game_field)
            if vyhodnot(o_game_field) != '-':
                break
            elif o_game_field:
                game_field = o_game_field
