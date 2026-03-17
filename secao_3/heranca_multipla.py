# Fazendo Herança Multipla e Multinivel com Exemplos


# Classes pai
class Predador():
  def cacando(self):
    print(f'Este animal está caçando!')

class Presa():
  def fugindo(self):
    print(f'Este animal sendo caçado!')

# classes filho
class Coelho(Presa):
  pass

class Tigre(Predador):
  pass

class Golfinho(Predador, Presa): # herança multipla
  pass

coelho1 = Coelho()
coelho1.fugindo()

tigre1 = Tigre()
tigre1.cacando()

golfinho1 = Golfinho()
golfinho1.cacando()
golfinho1.fugindo()

#
