from ai import random_word, field
from hangman_extension import input_control, result
from pictures import picture


def new_game():
    '''Nabidne hraci novou hru'''
    yes = ('a', 'ano')
    answer = input('Chces hrat znova? A/N: ').lower()
    hangman_game() if answer in yes else exit()


def hangman_game():
    words = ['kolotoc', 'ananas', 'krakatice']
    game_word = random_word(words)  # Vybere nahodne slovo ze seznamu
    game_field = field(game_word)  # Vypocita hraci pole
    mistakes = 0
    print(game_field)  # Vytiskne hraci pole

    while True:
        # Jestlize hrac vyhral, pocitac nabidne novou hru
        if result(game_field) == 'x':
            new_game()
        else:
            # Vyhodnoti, jestli je pismeno v hledanem slove
            new_game_field = input_control(game_field, game_word)
        # Jestlize neni pismeno v hledanem slove, pripocita se chybny tah
        if new_game_field is None:
            mistakes += 1
            # Vytiskne sibenici podle poctu chybnych tahu
            picture(mistakes)
            print(game_field)
            if mistakes == 9:
                print(f'Prohral jsi. Hledane slovo je: {game_word}')
                # Jeslize hrac prohral, pocitac nabidne novou hru
                new_game()
        else:
            # Jestlize bylo pismeno v hledanem slove, prepise se hraci pole
            print(new_game_field)
            game_field = new_game_field
