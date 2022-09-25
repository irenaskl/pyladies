# Zkus program „šťastná/bohatá“ přepsat pomocí zanořených ifů. Která verze ti připadá čitelnější?

print('Odpovidej pouze "ano" nebo "ne".')

stastna = input('Jsi stastna? ')
bohata = input('Jsi bohata? ')

if (stastna == 'ano' or stastna == 'Ano'):
    if (bohata == 'ano' or bohata == 'Ano'):
        print('Gratuluji!')
    else:
        if (bohata == 'ne' or bohata == 'Ne'):
            print('Zkus min utracet!')
        else:
            print('Nerozumim')        
else: 
    if (stastna == 'ne' or stastna == 'Ne'):
        if (bohata == 'ne' or bohata == 'Ne'): 
            print('To je mi lito.')
        else:  
            if (bohata == 'ano' or bohata == 'Ano'):    
                print('Zkus se vice usmivat.')
            else:
                print('Nerozumim.')  
    else: 
        print('Nerozumim')                  


 



    