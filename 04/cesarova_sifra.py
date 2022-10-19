from string import ascii_lowercase, ascii_uppercase

plaintext = input('Jaky mam zasifrovat text? ')
ciphertext = ''

while True:
    #Jestlize odpoved neni cislo, tak se dotaz opakuje
    key = (input('Jaky mam zadat klic? Zadej cele cislo: '))
    if key.isnumeric():
        key = int(key)
        break


for pismeno in plaintext:
    #jestlize je pismeno v abecede
    if pismeno in (ascii_uppercase[:26]):
        #prevede pismeno na znak
        znaky = (ord(pismeno)) - (ord('A'))
        #print(znaky)
        #prevede znak na pozadovanou sifru
        ci = (znaky + key) % 26
        ci = (ci + (ord('A')))
        #print(ci)
        ciphertext += (chr(ci))
    elif pismeno in (ascii_lowercase[:26]):
        #prevede pismeno na znak
        znaky = (ord(pismeno)) - (ord('a'))
        #print(znaky)
        #prevede znak na pozadovanou sifru
        ci = (znaky + key) % 26
        ci = (ci + (ord('a')))
        #print(ci)
        ciphertext += (chr(ci))

    else:
        ciphertext += pismeno

        

print(f"Zde je zasifrovany text: {ciphertext}")    






