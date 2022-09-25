# Zkus program „šťastná/bohatá“ přepsat pomocí zanořených ifů. Která verze ti připadá čitelnější?

print('Odpovidej pouze "ano" nebo "ne".')

stastna = input('Jsi stastna? ')
bohata = input('Jsi bohata? ')

if (stastna == 'ano' or stastna == 'Ano'):
    if (bohata == stastna):
        print('Gratuluji!')
    if (stastna == 'ano' or stastna == 'Ano'):
        if (bohata == 'ne' or bohata == 'Ne'):
            print('Zkus min utracet!')
else: 
    if (stastna == 'ne' or stastna == 'Ne'):
        if (bohata == stastna): 
            print('To je mi lito.')
        if (stastna == 'ne' or stastna == 'Ne'): 
            if (bohata == 'ano' or bohata == 'Ano'):    
                print('Zkus se vice usmivat.')
    else:
        print('Nerozumim.')

 



    