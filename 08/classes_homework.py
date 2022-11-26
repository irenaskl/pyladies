# Napiš si třídy pro cokoliv chceš tak, aby splňovaly zadání:
# Dvě (nebo více) odvozených tříd.
# Jedna odvozená třída bude kompletně přepisovat metodu nadřazené třídy.
# Druhá odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super().
# Obě odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc
# jiným způsobem (koťátko mňouká, štěňátko štěká).


class Printers:
    def __init__(self, name):
        self.name = name


    def printing_material(self):
        '''Vyhodnocuje mnozstvi tiskarskeho materialu (naplne)'''
        return self.printing_material > 0


    def production(self, product):
        '''Vypise, jaky produkt tiskarna tiskne.'''
        print(f'{self.name} is printing {product}...')


    def fill_paper(self, paper):
        '''Vypise hlasku, ze zasobnik papiru je prazdny.'''
        if paper == self.empty_paper:
            print(f'{self.name}: Stack is empty. Fill the paper.')


class InkPrinter(Printers):
    def __init__(self, name):
        # Rozsiruje metodu nadrazene tridy
        self.empty_paper = 0
        super().__init__(name)


    # Tridy maji stejnou metodu, ktera dela stejnou
    # vec jinym zpusobem:
    def fill_printing_material(self, material='ink'):
        '''Jestlize je napln pod hodnotou 0, vypise se hlaska'''
        if self.printing_material == False:
            print(f'{self.name}: Please, fill {material}.')


class LaserPrinter(Printers):
    def __init__(self, name):
        # Rozsiruje metodu nadrazene tridy
        self.empty_paper = 0
        super().__init__(name)


    def fill_printing_material(self, material='toner'):
            if self.printing_material == False:
                print(f'{self.name}: Please, change {material}.')

    # Tridy maji stejnou metodu, ktera dela stejnou
    # vec jinym zpusobem:
class Printer3D(Printers):
    def fill_printing_material(self, material='string'):
        '''Jestlize je napln pod hodnotou 0, vypise se hlaska'''
        if self.printing_material == False:
            print(f'{self.name}: Shitty job! No {material}!')

    # Jedna odvozena trida kompletne prepisuje metodu nadrazene tridy:
    def fill_paper(self, paper=0):
        '''3D tiskarna nepouziva papir, proto neni potreba vyhodnocovat stav.'''
        return None




if __name__ == "__main__":
    printer_list = [InkPrinter('Ink100'), LaserPrinter('Laser100'), Printer3D('3D100')]

    for printer in printer_list:
        printer.printing_material = 0
        printer.production('dragon')
        printer.fill_printing_material()
        printer.fill_paper(0)
