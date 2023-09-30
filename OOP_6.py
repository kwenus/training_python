
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        print(f'{self.name} wears {self.size} clothes')

class Parrot(Bird):
    def __init__(self, name, size, sound):
        super().__init__(name, size)
        self.sound = sound

    def show(self):
        print(f'{self.name} wears {self.size} clothes and {self.sound}')

sparrow = Bird('Sparrow', 'S')
ara = Parrot('Ara', 'XL', 'speak')
nymph = Parrot('Nymph', "XS", 'roar')

sparrow.show()
ara.show()
nymph.show()