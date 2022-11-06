
from string import ascii_lowercase


def change(game_field, game_random_word):
    '''Vymeni pismeno za '-' '''

    while True:      # Overeni vstupu
        letter = input('Zadej pismeno: ').lower()
        if letter in ascii_lowercase and len(letter) == 1:      # Jestlize neni pismeno v abecede
            break
        print('Toto neni jedno pismeno!')

    correct_letter = letter in game_random_word      # Pismeno je v hledanem slove

    if correct_letter:
        position = -1  
        for i in game_random_word:       # Vypocet pozice pismene v hracim slove
            position += 1
            if i == letter:
                break

        start = game_field[:position]      # Vymena '-' za pismeno
        end = game_field[position + 1:]
        new_field = start + letter + end
        return result(new_field)


def result(game_field):
    '''Vyhodnoti stav hry'''     # Jestlize uz neni volne '-', hra skonci, v opacnem pripade hra pokracuje.
    if '-' not in game_field:
        print('Gratuluji')
        exit(0)
    else:
        return game_field
