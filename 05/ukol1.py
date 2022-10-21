#Napiš program, který vypíše jména domácích zvířat (zadaných argumentem), která jsou
#kratší než 5 písmen.

list = ['pes', 'kocka', 'kralik', 'had',]
short = []

for i in list:
    if len(i) < 5:
        short.append(i)

print(f'Zvirata kratsi nez 5 pismen: {short}')     