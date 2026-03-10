class Pessoa:
  def __init__ (self, nome, idade, cargo):
    self.nome = nome
    self.idade = idade
    self.cargo = cargo

  def informacoes(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.idade}')
    print(f'Cargo: {self.cargo}')

  def promover(self, novo_cargo):
    print(f'{self.nome} foi poromovido(a) para a nova funcao de {novo_cargo}!')

colaborador1 = Pessoa('Ana', 36, 'Assistente Jr')
colaborador2 = Pessoa('Joao', 45, 'Dev Jr')

colaborador1.informacoes()
colaborador1.promover('Assistente Pleno')
