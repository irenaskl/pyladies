#Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
#herní pole se zaznamenaným tahem počítače.
#Použij jednoduchou náhodnou „strategii”:
#1. Vyber číslo od 0 do 19.
#2. Pokud je dané políčko volné, hrej na něj.
#3. Pokud ne, opakuj od bodu 1.

from random import randrange
def tah_pocitace(field):
    '''Vrati herni pole se zaznamenanym tahem pocitace.'''
    while True:
        pc_position = randrange(20)
        if field[pc_position] == '-':
            return tah(field, pc_position, 'o')

