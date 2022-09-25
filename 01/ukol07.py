# Spocitej povrch a objem krychle
# Změň program tak, aby stranu/poloměr mohl uživatel zadat.

strana = float(input('Zadej delku strany: '))

print('Povrch krychle pri delce strany ', strana, 'cm, je ', 6 * (strana * strana), 'cm2.')
print('Objem krychle pri delce strany ', strana, 'cm, je ', (strana * strana * strana), 'cm3.')