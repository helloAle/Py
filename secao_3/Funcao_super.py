# sobre a função super()

# SISTEMA DE ESCOLA
# preciso criar classes para diferentes cargos, pessoas
# classe filha sobrepoe classe mae

class Escola():
  def __init__(self, nome, idade, status):
    self.nome = nome
    self.idade = idade
    self.status = status

  def Apresentar(self):
    print(f'\nMeu nome é {self.nome}!')

  def Verificar_status(self):
    # print(f'Status: {self.status}')
    print(f'Status: {"ATIVO" if self.status else "INATIVO"}') #se o status for True, retorna ATIVO, se não, INATIVO

# classes filhas
class Aluno(Escola):
  def __init__(self, nome, idade, status, ano):
    super().__init__(nome, idade, status)
    self.ano = ano

  def Apresentar(self):
    super().Apresentar() #executa a função de mesmo nome da classe mae e filha
    print(f'\nMeu nome é {self.nome} e tenho {self.idade} anos de idade!')

class Professor(Escola):
  def __init__(self, nome, idade, status, materia):
    super().__init__(nome, idade, status)
    self.materia = materia

  def Apresentar(self):
    super().Apresentar() #executa a função de mesmo nome da classe mae e filha
    print(f'\nMeu nome é {self.nome} e leciono {self.materia}!')


class Assistente(Escola):
  def __init__(self, nome, idade, status, bloco):
    super().__init__(nome, idade, status)
    self.bloco = bloco

  def Apresentar(self):
    super().Apresentar() #executa a função de mesmo nome da classe mae e filha
    print(f'\nMeu nome é {self.nome} e sou assistente no Bloco {self.bloco}!')

a1 = Aluno( nome = 'Marcos', idade = 12,status = True, ano = 8)
p1 = Professor('Roberto', 34, True, 'Geometria')
as1 = Assistente('Ana Maria', 29, False, 'C')

a1.Apresentar()
a1.Verificar_status()

p1.Apresentar()
p1.Verificar_status()

as1.Apresentar()
as1.Verificar_status()

