
retezec = input('Zadej puvodni retezec: ')
pozice = int(input('Na jake pozici provedeme vymenu? '))
znak = input('Jaky znak tam dame? ')

print('Po vymene to vypada takto: ')
print(retezec[:pozice] + znak + retezec[pozice  + 1:])