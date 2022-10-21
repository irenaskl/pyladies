#Napiš program, který vypíše jména domácích zvířat, která začínají na k.

list = ['pes', 'kocka', 'kralik', 'had',]
k_list = []

for i in list:
    if i[0] == 'k':
        k_list.append(i)

print(f'Zvirata zacinajici na pismeno k: {k_list}')