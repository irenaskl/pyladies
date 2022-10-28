#Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
#herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.
#Hlavička funkce by tedy měla vypadat nějak takhle:
#def tah(pole, cislo_policka, symbol):
#"Vrátí herní pole s daným symbolem umístěným na danou pozici"

def tah(field, position, symbol):
    '''Umisteni tahu do herniho pole.'''
    start = field[:position]
    end = field[position + 1:]
    if (position >= 0 and position <= 19 and 
        symbol == 'x' or symbol == 'o'):
        change = start + symbol + end 
        return change    
    else:
        return False    


print(tah('------xx-o------', 2, 'x'))   
print(tah('------xx-o------', 20, 'x'))
print(tah('------xx-o------', 2, 'a'))

