# Polymorphism sem herança

class Cachorro:
    def emitir_som(self):
        print(f'Au Au')

class Gato:
    def emitir_som(self):
        print(f'MIAAAAAU')

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()
