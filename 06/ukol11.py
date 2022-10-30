#Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
#a vrátí herní pole se zaznamenaným tahem hráče.
#Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel
#zadá špatný vstup, funkce mu vynadá a zeptá se znova.

def tah_hrace(field):
    '''Vrati herni pole se zaznamenanym tahem hrace.'''
    while True:
        player_position = int(input('Zadej cislo pozice: '))
        if (player_position >= 0 and player_position <= 19 and 
           field[player_position] == '-'):
           return tah(field, player_position, 'x' )    
        print('Spatne zadana pozice.')
       
         

print(tah_hrace('------xx-o------'))
