
from string import ascii_lowercase


def change(game_field, game_random_word):
    '''Vymeni pismeno za '-' '''

    while True:  # Overeni vstupu
        letter = input('Zadej pismeno: ').lower()
        # Jestlize je pismeno v abecede a ma 1 znak.
        if letter in ascii_lowercase and len(letter) == 1:
            break
        print('Toto neni jedno pismeno!')

    # Pismeno je v hledanem slove
    correct_letter = letter in game_random_word

    if correct_letter:
        # Vypocet pozice pismene v hracim slove
        position = game_random_word.index(letter)

        start = game_field[:position]  # Vymena '-' za pismeno
        end = game_field[position + 1:]
        new_field = start + letter + end
        return result(new_field)


def result(game_field):
    '''Vyhodnoti stav hry'''
    # Jestlize uz neni volne '-', hra skonci, v opacnem pripade hra pokracuje.
    if '-' not in game_field:
        print('Gratuluji')
        exit(0)

    return game_field
