#Napiš tyto programy. Každý z nich bude mít na vstupu řetězec s rodným číslem a nějak ho
#zanalyzuje:
#(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vypíše True nebo False)
#(b) Je dělitelné jedenácti? (vypíše True nebo False)
#(c) Jaké datum narození je v čísle zakódováno? (vypíše trojici čísel – den, měsíc, rok)
#(d) Jaké pohlaví je v čísle zakódováno? (vypíše 'muž' nebo 'žena')
#Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985.
#Reálná rodná čísla můžou být složitější :)



#Osetreni vstupu
while True:
    pin = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ') 
    if pin.replace('/','',1).isdigit():
        break
    print('Toto neni cislo!')

#Pin musi mit 11 znaku, na seste pozici musi byt /, kdyz se lomitko na prvni pozici nahradi "", tak musi byt pin cislo.
if len(pin) == 11 and pin[6] == '/' and pin.replace('/','',1).isdigit():
    print(True)
else:
    print(False)    

pin = pin.replace('/','',1)         #Prvni pozici se znakem / vymenim za ""
pin_int = int(pin)                  #Rodne cislo prevedu ze string na cislo
result = pin_int / 11               #Rodne cislo vydelim 11 se zbytem

if result == int(result):           #Vysledek musi byt cele cislo
    #print(result)
    print(True)
else:
    print(False) 

date = pin[4:6]
month = int(pin[2:4])
year = int(pin[:2])

#print(type(month))

sex = 'Muz'

#print(month[:1])
if month > 12:
    month = month - 50
    sex = 'Zena'

century = '19'
if year <= 22:
    century = '20'


print(f'Datum narozeni: {date}.{month}.{century}{year}')    
print(sex)
     

    



#print(date, month, year) 