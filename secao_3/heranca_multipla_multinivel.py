# Fazendo Herança Multipla e Multinivel com Exemplos

# classe Avo
class Animal:
  def __init__(self, nome):
    self.nome = nome


# Classes pai
class Predador(Animal):
  def cacando(self):
    print(f'O {self.nome} está caçando!')

class Presa(Animal):
  def fugindo(self):
    print(f'O {self.nome} está sendo caçado!')

# classes filho
class Coelho(Presa):
  pass

class Tigre(Predador):
  pass

class Golfinho(Predador, Presa): # herança multipla
  pass

coelho1 = Coelho('Coelho')
tigre1 = Tigre('Tigre')
golfinho1 = Golfinho('Golfão')

coelho1.fugindo()
tigre1.cacando()
golfinho1.cacando()
golfinho1.fugindo()

#
