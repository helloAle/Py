# polimorfismo :D

class Personagem():
    def falar(self):
        print(f'Eu sou um personagem!!')

class Guerreiro(Personagem):
    def falar(self):
        print(f'Eu sou um guerreiro!!')

class Mago(Personagem):
    def falar(self):
        print(f'Eu sou um Mago!!')

class Arqueiro(Personagem):
    def falar(self):
        print(f'Eu sou um Arqueiro!!')

# criar os objetos

personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.falar()
