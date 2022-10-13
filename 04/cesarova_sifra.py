from string import ascii_lowercase, ascii_uppercase

plaintext = input('Jaky mam zasifrovat text? ')
ciphertext = ''

#while key != int():
key = int(input('Jaky mam zadat klic? Zadej cele cislo: '))


for pismeno in plaintext:
    #jestlize je pismeno v abecede
    if pismeno in (ascii_lowercase[:26] + ascii_uppercase[:26]):
        #prevede pismeno na znak
        znaky = (ord(pismeno))
        #prevede znak na pozadovanou sifru
        ciphertext += (chr(znaky + key))
    else:
        ciphertext += pismeno

        

print(f"Zde je zasifrovany text: {ciphertext}")    






