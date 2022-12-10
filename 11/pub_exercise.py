
numbers = ['1331', '2332', '1771', '1234', '5678', '131131', '13331', '10301']
palindrom = []
palindrom_int = map(int, palindrom)
not_prime_number = []

for i in numbers:
    if i == i[::-1]:
        palindrom.append(i)

print(palindrom)

for i in palindrom_int:
    count = list(range(2, i))
    for n in count:
        result = (i % n)
        if result == 0:
            i = str(i)
            not_prime_number.append(i)
            break

for i in not_prime_number:
    if i in palindrom:
        palindrom.remove(i)

print(f'Numbers are palindrom and prime numer: {palindrom}')
