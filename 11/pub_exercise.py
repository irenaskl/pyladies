
list = ['1331', '2332', '1771', '1234', '5678']
palindrom = []
palindrom_int = map(int, palindrom)
prime_numbers = []
not_prime_number = []
count = [2, 3, 4, 5, 6, 7, 8, 9]

for i in list:
    if i == i[::-1]:
        palindrom.append(i)


for i in palindrom_int:
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
