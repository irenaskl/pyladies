#Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.

cisla = []
for i in range(5):
    vstup = int(input(f"Zadej {i + 1}. číslo: "))
    cisla.append(vstup)

print(f"Nejmenší číslo jest: {min(cisla)}")

#Ve výrazech v chlupatých závorkách {...} v f-stringu lze normálně volat třeba i
#funkce. V tomhle případě jsme použili vestavěnou funkci min(), které
#podstrčíme nějaký iterable (iterable je něco, přes co se dá iterovat - tedy např. list,
#string, tuple, dokonce aj slovník nebo set) - a z funkce se pak vrátí prvek, který má
#v celém iterable nejnižší hodnotu.