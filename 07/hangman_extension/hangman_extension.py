from string import ascii_lowercase


def input_control(game_field, game_random_word):
    '''Overi validitu vtupu'''
    while True:  # Overeni vstupu
        letter = input('Zadej pismeno: ').lower()
        # Jestlize je pismeno v abecede a ma 1 znak.
        if letter in ascii_lowercase and len(letter) == 1:
            return position(game_field, game_random_word, letter)
        print('Toto neni jedno pismeno!')


def position(game_field, game_random_word, letter):
    '''Vypocita pozice pismena v hledanem slove'''
    # Pismeno je v hledanem slove
    correct_letter = letter in game_random_word

    if not correct_letter:
        return None

    counter = -1
    more_positions = []
    # Vypocet pozic pismene v hledanem slove
    for i in game_random_word:
        counter += 1
        if i == letter:
            x = game_random_word.index(letter, counter)
            more_positions.append(x)
    return change(game_field, letter, more_positions)


def change(game_field, letter, positions):
    '''Vymeni pismeno za '-' '''
    new_field = game_field
    for i in positions:
        start = new_field[:i]  # Vymena '-' za pismeno
        end = new_field[i + 1:]
        new_field = start + letter + end
    return result(new_field)


def result(game_field):
    '''Vyhodnoti stav hry'''
    # Jestlize uz neni volne '-', hra skonci, v opacnem pripade hra pokracuje.
    if '-' not in game_field:
        print(game_field)
        return 'Gratuluji!'

    return game_field
