#Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
#herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.
#Hlavička funkce by tedy měla vypadat nějak takhle:
#def tah(pole, cislo_policka, symbol):
#"Vrátí herní pole s daným symbolem umístěným na danou pozici"

def tah(field, position, symbol):
    '''Vrati herni pole s danym symbolem umistenym na danou pozici.'''
    correct_position = position in range (0, 20)
    correct_symbol = symbol == 'x' or symbol == 'o'
    if not correct_position or not correct_symbol:
        return False   
    
    start = field[:position]
    end = field[position + 1:]
    return start + symbol + end


