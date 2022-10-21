#Napiš program, kde budou na začátku dva seznamy jmen vypíše a vrátí tři seznamy:
#(a) zvířata, která jsou v obou seznamech (sjednocení množin: první ∪ druhá),
#(b) zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
#(c) zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).

list1 = ['cat', 'dog', 'rabbit', 'snake']
list2 = ['cow', 'pig', 'chicken', 'snake']
a_list = []
b_list = []
c_list = []

for i in list1 + list2:
    if i in list1 and i in list2:
        a_list.append(i)
    elif i in list1:
        b_list.append(i)
    elif i in list2:
        c_list.append(i)

x = [*set(a_list)] #vytvori novy a_list bez duplicit

print(f'Zvirata, ktera jsou v obou seznamech: {x}')
print(f'Zvirata, ktera jsou v prnim seznamu: {b_list}')
print(f'Zvirata, ktera jsou v druhem seznamu: {c_list}')