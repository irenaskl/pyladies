from random import randrange
from util import tah


def tah_pocitace(field):
    '''Vrati herni pole se zaznamenanym tahem pocitace.'''
    while True:
        pc_position = randrange(20)
        if field[pc_position] == '-':
            return tah(field, pc_position, 'o')
