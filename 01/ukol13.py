# Na srazu jsme měli program, který píše různé nesmysly podle uživatelem zadaného věku.
# Zkus napsat program, který píše hlášky podle zadané rychlosti chůze, váhy ulovené ryby, počtu tykadel,
# teploty vody nebo třeba vzdálenosti od rovníku.


vaha = int(input('Jak tezkou rybu (kg) jsi chytil?'))

if vaha >= 10:
    print('Nez ji celou snis, zkazi se! Pust ji zpatky.')
elif vaha >= 3:
    print('Tyto ryby splni 3 prani. Pust ji zpatky.')
elif vaha >= 1:
    print('Sama kost. Pust ji zpatky.')
else:
    print('Bez si radeji zaplavat.')        

