from random import choice


def random_word(game_list):
    '''Pocitac vybere z globalniho seznamu nahodne slovo.'''
    game_random_word = choice(game_list)  # Vybere nahodne slovo ze seznamu
    return game_random_word               # Vyvola funkci field pro vypocet hraciho pole


def field(game_random_word):
    '''Nastavi retezec s tolika pomlckami, kolik ma slovo.'''
    game_field = len(game_random_word) * '-'  # Spocita pocet pismen ve slove a vypise stejny pocet '-'
    return game_field
