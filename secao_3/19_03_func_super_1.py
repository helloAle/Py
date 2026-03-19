# sobre a função super()

# SISTEMA DE ESCOLA
# preciso criar classes para diferentes cargos, pessoas


class Aluno():
  def __init__(self, nome, idade, ano):
    self.nome = nome
    self.idade = idade
    self.ano = ano

  
class professor():
  def __init__(self, nome, idade, materia):
    self.nome = nome
    self.idade = idade
    self.materia = materia


class Assistente():
  def __init__(self, nome, idade, bloco):
    self.nome = nome
    self.idade = idade
    self.bloco = bloco
    
a1 = Aluno('Marcos', 12, 8)
# print(f'{a1.nome}')
print(a1.nome)
print(a1.idade)
print(a1.ano)


# problema do codigo: codigo nao segmentado, a estrutura nao está bem feita
