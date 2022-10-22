#Napiš program který se uživatele zeptá na rodné číslo a vypíše, zda zadal rodné
#číslo správně (Využije výsledky z úkolu 7).

while True:
    pin = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ') 
    if pin.replace('/','',1).isdigit():
        break
    print('Toto neni cislo ve formatu xxxxxx/xxxx!')

#Pin musi mit 11 znaku, na seste pozici musi byt /, kdyz se lomitko na prvni pozici nahradi "", tak musi byt pin cislo.
if len(pin) == 11 and pin[6] == '/' and pin.replace('/','',1).isdigit():
    True
else:    
    print('Spatny format rodneho cisla.')    

pin = pin.replace('/','',1)         #Prvni pozici se znakem / vymenim za ""
pin_int = int(pin)                  #Rodne cislo prevedu ze string na cislo
result = pin_int / 11               #Rodne cislo vydelim 11 se zbytem


if result == int(result):           #Vysledek musi byt cele cislo
      print('Spravne zadane rodne cislo.')  
else:
    print('Spatne zadane rodne cislo.')

