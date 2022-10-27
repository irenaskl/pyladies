#Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".
#Abys hada uklidnila, vytvoř program, který zvířata seřadí podle abecedy, ale bude
#ignorovat první písmeno
#(t.j. vypíše ["had", "pes", "andulka", "kočka", "králík"])

list = ['pes', 'kocka', 'kralik', 'had',]
list.append('andulka')

list.sort(key=lambda animal : animal[1:])

print(list)
