#Napis tyto funkce. Každá z nich dostane jako argument řetězec s rodným číslem a nějak ho zanalyzuje:
#(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False)
#(b) Je dělitelné jedenácti? (vrací True nebo False)
#(c) Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
#(d) Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')
#Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985. 
# Reálná rodná čísla můžou být složitější :)

from curses.ascii import isdigit
from datetime import datetime

def format(eleven_char):
    '''Overi validitu formatu rodneho cisla'''
    return (len(eleven_char) == 11 and eleven_char[6] == '/' and
            eleven_char.replace('/', '', 1).isdigit())

def devide(eleven_char):
    '''Overi delitelnost rodneho cisla jedenacti.''' 
    eleven_char = eleven_char.replace('/','',1)  
    eleven_char_int = int(eleven_char)
    return eleven_char_int % 11 == 0

def date_of_birth(eleven_char):
    '''Z rodneho cisla vypocita datum narozeni.'''
    day = eleven_char[4:6]
    if int(eleven_char[4]) < 1:
        day = eleven_char[5]
    month = int(eleven_char[2:4])
    year = int(eleven_char[:2])   
    current_year_full = datetime.now().year
    current_century = int(str(current_year_full)[:2])
    current_year = int(str(current_year_full)[2:])
    year_full = (current_century if year <= current_year else current_century - 1) * 100 + year
    if month > 12:
        month = month - 50
    date = f'{day}.{month}.{year_full}'
    return date

def sex(eleven_char):
    '''Z rodneho cisla zjisti pohlavi.'''
    month = int(eleven_char[2:4])
    sex = 'Muz'
    if month > 12:
        month = month - 50
        sex = 'Zena'
    return sex    
    

#Osetreni vstupu
while True:
    pin = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ') 
    if pin.replace('/', '', 1).isdigit():
        break
    print('Toto neni cislo ve formatu xxxxxx/xxxx!')


has_correct_format = format(pin)
print('Kontrola formatu cisla:', has_correct_format)
if not has_correct_format:
    exit(1)

has_correct_divisibility = devide(pin)   
print('Delitelnost 11:', has_correct_divisibility)
if not has_correct_divisibility:
    exit(2) 

print('Datum narozeni:', date_of_birth(pin))
print('Pohlavi:', sex(pin))

