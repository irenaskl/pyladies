#Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec – buď '+', '-', '*'
#nebo '/'. Program provede na číslech příslušnou operaci.

prvni = int(input('Zadej prvni cislo: '))
operace =input('Zadej matematicke znamenko: ')
druhe = int(input('Zadej druhe cidlo: '))

if operace == '+':
    vysledek = (f'{prvni + druhe}')
    print(f'{prvni} + {druhe} = {vysledek}')
elif operace == '-':
    vysledek = (f'{prvni - druhe}')
    print(f'{prvni} - {druhe} = {vysledek}')  
elif operace == '*':
    vysledek = (f'{prvni * druhe}')
    print(f'{prvni} * {druhe} = {vysledek}')  
elif operace == '/':
    vysledek = (f'{prvni / druhe}')
    print(f'{prvni} / {druhe} = {vysledek}')      



