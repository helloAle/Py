class Pessoa:
  def __init__ (self, nome, idade):
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade.')


class Funcionario(Pessoa):
  def __init__ (self, nome, idade, cargo):
    super().__init__(nome, idade)
    self.cargo = cargo

  def trabalhar(self):
    print(f'{self.nome} está trabalhando como {self.cargo}.')

class Cliente(Pessoa):
  def __init__ (self, nome, idade, saldo):
    super().__init__(nome, idade)
    self.saldo = saldo

  def comprar(self, valor_compra):
    if valor_compra <= self.saldo:
      self.saldo -= valor_compra
      print(f'Olá {self.nome}!\nA sua compra de {valor_compra} foi aprovada! seu saldo atual é de: ${self.saldo}')
    else:
      print(f'Olá {self.nome}!\nSaldo insuficiente')

f1 = Funcionario('Maria', 38,'gerente')
# f1.apresentar()
# f1.trabalhar()

c1 = Cliente('artur', 17, 200)
c2 = Cliente('martha', 45, 2000)
# c1.apresentar()
c1.comprar(201)
c2.comprar(1000)
