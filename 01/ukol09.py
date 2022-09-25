# Zkombinuj program z předchozího projektu s programem kámen-nůžky-papír a nastav tah_pocitace na:
# (a) 'kámen', pokud je cislo 0,
# (b) 'nůžky', pokud je cislo 1,
# (c) jinak na 'papír'.

from random import randrange
cislo = randrange(3)
#print(cislo)

if cislo == 0: 
    print('kamen')
elif cislo == 1:
    print('nuzky')
else: 
    print('papir')    

