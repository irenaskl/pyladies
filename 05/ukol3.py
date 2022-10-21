
#Napiš program, který dostane slovo a zjistí, jestli je v seznamu domácích zvířat.
#„Zjistí“ znamená, že vrátí True nebo False.

list = ['pes', 'kocka', 'kralik', 'had',]

while True:
    new = input('Napis slovo: ') in list
    print(new)
    break
    
   