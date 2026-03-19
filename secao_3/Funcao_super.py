# sobre a função super()

# SISTEMA DE ESCOLA
# preciso criar classes para diferentes cargos, pessoas
# classe filha sobrepoe classe mae

class Escola():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def Apresentar(self):
    print(f'Meu nome é {self.nome}!')

# classes filhas
class Aluno(Escola):
  def __init__(self, nome, idade, ano):
    super().__init__(nome, idade)
    self.ano = ano

  def Apresentar(self):
    super().Apresentar() #executa a função de mesmo nome da classe mae e filha
    print(f'Meu nome é {self.nome} e tenho {self.idade} anos de idade!')
  
class Professor(Escola):
  def __init__(self, nome, idade, materia):
    super().__init__(nome, idade)
    self.materia = materia


class Assistente(Escola):
  def __init__(self, nome, idade, bloco):
    super().__init__(nome, idade)
    self.bloco = bloco
    
a1 = Aluno('Marcos', 12, 8)
p1 = Professor('Roberto', 34, 'Geometria')
as1 = Assistente('Ana Maria', 29, 'C')

a1.Apresentar()

