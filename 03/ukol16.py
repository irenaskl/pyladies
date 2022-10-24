#Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec – buď '+', '-', '*'
#nebo '/'. Program provede na číslech příslušnou operaci.


# Zkontrolujeme vstup validního čísla - první číslo.
while True:
  prvni = input('Zadej prvni cislo: ')
  if prvni.replace('.', '',1).isdigit():
    break
  print("To neni cislo!")

# Zkontrolujeme vstup validního znaménka.
while True:
  operace = input('Zadej matematicke znaménko: ')
  if len(operace) == 1 and operace in "+-/*":  # Chytré, že? :D Kontrolujeme, zda je to jeden znak - a zda ten jeden znak je obsažený ve stringu "+-/*", což ve výsledku prostě řekne, jestli je to jeden znak z těch námi povolených.
    break
  print("Tohle znaménko neznám, sakra.")

# Zkontrolujeme vstup validního čísla - druhé číslo.
while True:
  druhe = input('Zadej druhé číslo: ')
  if druhe.replace('.', '',1).isdigit():
    break
  print("To neni cislo!")

# A stringy s číslem převedeme na správný datový typ (chceme umět i desetinná čísla, takže spíš float).
prvni = float(prvni)
druhe = float(druhe)

# Ale zase pokud ten float reálně obsahuje celé číslo, tak to hodíme zas na int.
prvni = int(prvni) if prvni.is_integer() else prvni  # Do proměnné 'prvni' se uloží hodnota z proměnné 'prvni' přetypovaná na int, pokud výsledek 'prvni.is_integet()' vrátí True, jinak se do proměnné 'prvni' vloží hodnota proměnné 'prvni' (tzn. se vůbec nic nestane).
druhe = int(druhe) if druhe.is_integer() else druhe  # To samé jak předchozí řádek, jen pro proměnnou 'druhe'.
#Duvod, proc na konci resime prevod z float na int je ciste esteticky. Kdyby totiz cisla byla v datovem typu foat, tak je Python vypisuje s dessetinnou carkou.

if operace == '+':
    vysledek = prvni + druhe
elif operace == '-':
    vysledek = prvni - druhe 
elif operace == '*':
    vysledek = prvni * druhe
elif operace == '/':
    vysledek = prvni / druhe
    
print(f'{prvni} {operace} {druhe} = {vysledek}')      



