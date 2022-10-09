from random import *

print('Mas 0 bodu, davam prvni kartu.')

seznam = [1,7,8,9,10,11]
celkem = seznam[randrange(5)]


print('Mas ', celkem, ' bodu.')
odpoved = input('Chces dalsi kartu? Ano nebo Ne?: ') 
odpoved = odpoved.lower()

while odpoved == 'ano':
    dalsi_karta = seznam[randrange(5)]
    celkem = (celkem + dalsi_karta)
    print('Tvoje nova karta ma ', dalsi_karta, 'bodu. Celkovy pocet bodu je ', celkem, ' .')
    if celkem == 21:
        print('Vyhral jsi!')
        break
    if celkem >= 22:
        print('Vyhral pocitac.')
        break
    odpoved = input('Chces dalsi kartu? Ano nebo Ne?: ')
    odpoved = odpoved.lower()
while odpoved == 'ne':
    print('Vyhral jsi!')
    break
         