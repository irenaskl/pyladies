#Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
#a vrátí herní pole se zaznamenaným tahem hráče.
#Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel
#zadá špatný vstup, funkce mu vynadá a zeptá se znova.

def tah_hrace(field):
    '''Vrati herni pole se zaznamenanym tahem hrace.'''
    while True:
        player_position = input('Zadej cislo pozice: ')
        if player_position.isdigit():
            break
        print('Spatne zadana pozice.')

    while True:
        player_position = int(player_position)
        if (player_position in range(0, 20) and 
            field[player_position] == '-'):
           return tah(field, player_position, 'x' )    
        print('Spatne zadana pozice.')
        return tah_hrace(field)
         


