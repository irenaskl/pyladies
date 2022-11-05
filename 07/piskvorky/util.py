
def tah(field, position, symbol):
    '''Vrati herni pole s danym symbolem umistenym na danou pozici.'''
    correct_position = position in range(0, 20)
    correct_symbol = symbol == 'x' or symbol == 'o'
    if not correct_position or not correct_symbol:
        return False

    start = field[:position]
    end = field[position + 1:]
    return start + symbol + end
