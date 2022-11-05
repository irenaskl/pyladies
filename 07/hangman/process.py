from ai import random_word, field
from hangman import change
from pictures import picture


def hangman_game():
    words = ['kvetina', 'slunce', 'lasice']
    game_word = random_word(words)      # Vybere nahodne slovo ze seznamu
    game_field = field(game_word)       # Vypocita hraci pole
    mistakes = 0
    print(game_field)       # Vytiskne hraci pole

    while True:
        # Vyhodnoti, jestli je pismeno v hledanem slove
        new_game_field = change(game_field, game_word)
        if new_game_field == None:     # Jestlize neni pismeno v hledanem slove, pripocita se chybny tah
            mistakes += 1
            # Vytiskne sibenici podle poctu chybnych tahu
            picture(mistakes)
            print(game_field)
            if mistakes == 9:
                print(f'Prohral jsi. Hledane slovo je: {game_word}')
                exit(1)
        else:
            # Jestlize bylo pismeno v hledanem slove, prepise se hraci pole
            print(new_game_field)
            game_field = new_game_field


hangman_game()
