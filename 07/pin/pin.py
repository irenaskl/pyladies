
from datetime import datetime


def format(eleven_char):
    '''Overi validitu formatu rodneho cisla'''
    while True:
        eleven_char_int = eleven_char.replace('/', '', 1)
        try:
            int(eleven_char_int)
            break
        except ValueError:
            print('Toto neni cislo!')
            eleven_char = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ')

    return (len(eleven_char) == 11 and eleven_char[6] == '/' and
            eleven_char.replace('/', '', 1).isdigit())


def devide(eleven_char):
    '''Overi delitelnost rodneho cisla jedenacti.'''
    eleven_char = eleven_char.replace('/', '', 1)
    try:
        return eleven_char % 11 == 0
    except TypeError:
        eleven_char = int(eleven_char)
        return eleven_char % 11 == 0


def date_of_birth(eleven_char):
    '''Z rodneho cisla vypocita datum narozeni.'''
    day = eleven_char[4:6]
    if int(eleven_char[4]) < 1:
        day = eleven_char[5]
    month = int(eleven_char[2:4])
    year = int(eleven_char[:2])
    current_year_full = datetime.now().year
    current_century = int(str(current_year_full)[:2])
    current_year = int(str(current_year_full)[2:])
    year_full = (current_century if year <=
                 current_year else current_century - 1) * 100 + year
    if month > 12:
        month = month - 50
    date = f'{day}.{month}.{year_full}'
    return date


def sex(eleven_char):
    '''Z rodneho cisla zjisti pohlavi.'''
    month = int(eleven_char[2:4])
    sex = 'Muz'
    if month > 12:
        month = month - 50
        sex = 'Zena'
    return sex
