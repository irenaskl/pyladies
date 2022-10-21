
zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
chybne_zaznamy = []
spravne_zaznamy = []

for name in zaznamy:
    x = name.split()
    #print(x)
    iscorrect = True
    for word in x:
        if not word[0].isupper() or not word[1:].islower():
            iscorrect = False

    if iscorrect:
        spravne_zaznamy.append(name)
    else:
        chybne_zaznamy.append(name)


print(f'Chybne zaznamy: {chybne_zaznamy}')            
print(f'Spravne zaznamy: {spravne_zaznamy}')           

