#Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".
#Abys hada uklidnila, vytvoř program, který zvířata seřadí podle abecedy, ale bude
#ignorovat první písmeno
#(t.j. vypíše ["had", "pes", "andulka", "kočka", "králík"])

list = ['pes', 'kocka', 'kralik', 'had',]
list.append('andulka')
dictionary = {}
result = []


for word in list:
    dictionary[word[1:]] = word                 #V dictionary vytvari slovnik (slovo bez prvniho pismene: puvodni slovo)
sorted_dict = dict(sorted(dictionary.items()))  #Vytvori novy slovnik serazeny podle abecedy.

for value in sorted_dict.values():              #Kazda hodnota ze sorted_dict se ulozi do seznamu result.
    result.append(value)

print(result)

