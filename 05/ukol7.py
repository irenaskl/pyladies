#Napiš tyto programy. Každý z nich bude mít na vstupu řetězec s rodným číslem a nějak ho
#zanalyzuje:
#(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vypíše True nebo False)
#(b) Je dělitelné jedenácti? (vypíše True nebo False)
#(c) Jaké datum narození je v čísle zakódováno? (vypíše trojici čísel – den, měsíc, rok)
#(d) Jaké pohlaví je v čísle zakódováno? (vypíše 'muž' nebo 'žena')
#Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985.
#Reálná rodná čísla můžou být složitější :)

from datetime import datetime

#Osetreni vstupu
while True:
    pin = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ') 
    if pin.replace('/','',1).isdigit():
        break
    print('Toto neni cislo ve formatu xxxxxx/xxxx!')

#Pin musi mit 11 znaku, na seste pozici musi byt /, kdyz se lomitko na prvni pozici nahradi "", tak musi byt pin cislo.
if len(pin) == 11 and pin[6] == '/' and pin.replace('/','',1).isdigit():
    print('Kontrola formatu cisla: ', True)
else:
    print('Kontrola formatu cisla: ', False) 
    exit(1)   

pin = pin.replace('/','',1)         #Prvni pozici se znakem / vymenim za ""
pin_int = int(pin)                  #Rodne cislo prevedu ze string na cislo
         

if pin_int % 11 == 0:               #Vysledek musi byt cele cislo.
    print('Delitelnost 11: ', True)
else:
    print('Delitelnost 11: ',False) 
    exit(2)

day = pin[4:6]
month = int(pin[2:4])
year = int(pin[:2])
#print(type(month))
sex = 'Muz'

if month > 12:
    month = month - 50
    sex = 'Zena'

current_year_full = datetime.now().year
current_century = int(str(current_year_full)[:2])
current_year = int(str(current_year_full)[2:])
year_full = (current_century if year <= current_year else current_century - 1) * 100 + year


print(f'Datum narozeni: {day}.{month}.{year_full}')    
print('Pohlavi: ', sex)
     
