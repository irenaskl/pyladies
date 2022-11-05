# Přepiš program na kontrolu rodného čísla pomocí try/except bloků tam, kde to dává smysl.
# Cílem úkolu je, aby program nikdy neskončil výjimkou, ale vypsal hlášku,
# v případě že zadané rodné číslo není validní. V tom případě je také zbytečné
# vykonávat další funkce na kontrolu dělitelnosti a zjištění data narození a pohlaví.

from pin import format, devide, date_of_birth, sex

pin = input('Zadej rodne cislo ve formatu xxxxxx/xxxx: ')

has_correct_format = format(pin)
print('Kontrola formatu cisla:', has_correct_format)
if not has_correct_format:
    exit(1)

has_correct_divisibility = devide(pin)
print('Delitelnost 11:', has_correct_divisibility)
if not has_correct_divisibility:
    exit(2)

print('Datum narozeni:', date_of_birth(pin))
print('Pohlavi:', sex(pin))
