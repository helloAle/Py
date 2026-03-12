#  SOBRE HERANÇA

# permite ter uma classe, parametros e metodos
# ter outra classe e utilizar os parametros anteriores

#   classe Pai (x, y, z):
#     def 1
#     def 2
#     def 3

#   classe filho (Pai):
#      def 4
#      def 5
#      def 1

class Animal:
  def __init__ (self, nome, cor, especie):
    self.nome = nome
    self.cor = cor
    self.especie = especie

  def apresentar(self):
    print(f'Eu sou o {self.especie} chamado {self.nome}')

class Gato(Animal):
  def emitir_som(self):
    print('miau')

class Cachorro(Animal):
  def emitir_som(self):
    print('Au Au')

class Elefante(Animal):
  def emitir_som(self):
    print(':P')


gato1 = Gato('Felix', 'Branco', 'Siames')
gato1.apresentar()
gato1.emitir_som()

cachorro1 = Cachorro('Russo','preto','Pastor Alemão')
cachorro1.apresentar()
cachorro1.emitir_som()

elefante1 = Elefante('Fred','Marrom','Asiatico')
elefante1.apresentar()
elefante1.emitir_som()
