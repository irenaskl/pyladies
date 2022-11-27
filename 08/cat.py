class Cat:

    def __init__(self, name):
        self.name = name
        self.live = 9

    def meow(self):
        print(f'{self.name}: Meow!')

    def is_alive(self):
        return self.live > 0

    def loose_life(self):
        if self.live > 0:
            self.live -= 1

    def eat(self, food):
        if food == 'fish':
            if self.is_alive == True and self.live < 9:
                self.live += 1
