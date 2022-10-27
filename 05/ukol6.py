#Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".
#Abys hada uklidnila, vytvoř program, který zvířata seřadí podle abecedy, ale bude
#ignorovat první písmeno
#(t.j. vypíše ["had", "pes", "andulka", "kočka", "králík"])

list = ['pes', 'kocka', 'kralik', 'had',]
list.append('andulka')
key = []
result = []


for word in list:
    key.append([word[1:], word])    #V key seznamu vytvari jednotl.seznamy (slovo bez prvniho pismene + puvodni slovo)
    key.sort()  #V key seznamu seradi slova podle abecedy

for record in key:
    result.append(record[-1])   #Do seznamu result prida pouze druhe slovo z kazdeho seznamu v key seznamu
print(result)    
    