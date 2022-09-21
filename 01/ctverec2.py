strana = float(input('Zadej cislo strany: '))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod ctverce se stranou', strana, 'cm je', strana * 4, 'cm')
    print('Obsah ctverce se stranou', strana, 'cm je', strana * strana, 'cm2')
else:
    print('Strana musi byt kladna, jinak z toho nebude ctverec')

print('Dekujeme za pouziti geometricke kalkulacky')    

