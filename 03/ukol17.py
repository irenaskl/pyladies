#Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.

first_number = int(input('Zadej prvni cislo: '))
second_number = int(input('Zadej prvni cislo: '))
third_number = int(input('Zadej prvni cislo: '))
fourth_number = int(input('Zadej prvni cislo: '))
fifth_number = int(input('Zadej prvni cislo: '))

numbers = [first_number, second_number, third_number, fourth_number, fifth_number]

numbers.sort()


print(f'Nejmensi cislo ze seznamu je {numbers[:1]} .')

