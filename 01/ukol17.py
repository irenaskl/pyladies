# Zkus přepsat Kámen, Nůžky, Papír pomocí and a or.
# Dokážeš docílit toho, aby se každý z řetězců 'Plichta.', 'Počítač vyhrál.' a 'Vyhrála jsi!' objevil
# v programu jen jednou, aniž bys tyhle řetězce musela přiřazovat do proměnných?


clovek = input('Vyber kamen, nuzky nebo papir: ')

from random import randrange
pocitac = randrange(3)
#print(pocitac)

if pocitac == 0:
    pocitac = 'kamen' 
    print('kamen')
elif pocitac == 1:
    pocitac = 'nuzky'
    print('nuzky')
else: 
    pocitac = 'papir'
    print('papir')

# Souboj
if pocitac == clovek:
    print('Remiza')
elif ((pocitac == 'nuzky') and (clovek == 'papir')) or ((pocitac == 'papir') and (clovek == 'kamen')) or ((pocitac == 'kamen') and (clovek == 'nuzky')):
    print('Prohral jsi')
#elif ((pocitac == 'nuzky') and (clovek == 'kamen')) or ((pocitac == 'papir') and (clovek == 'nuzky')) or ((pocitac == 'kamen') and (clovek == 'papir')):
    #print('Vyhral jsi.')   
else:
    print('Vyhral jsi.')       



