from random import randint 

seznam = randint(2,10)
target_value = 21 
total = 0 

while True:
    print(f"Mas {total} bodu.")
    answer = input('Chces dalsi kartu? Ano nebo Ne?: ').lower()
    
    if answer == 'ano':
        total += randint(2,10)
        if total >= target_value:
            break

    elif answer == 'ne':
        break   

    else:
        print('Nerozumim.')

if total == target_value:
    print(f"Vyhral jsi! Mas {total} bodu.")
elif total < target_value:
    print(f"Mas pouze {total} bodu.")
else:
    print(f"Prohravas s {total} body.")        

 
         