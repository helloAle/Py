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

  def atualizar_idade(self, nova_idade):
    if nova_idade > self.idade:
      print(f'Atualizando a Idade de {self.idade} para {nova_idade}')
    else:
      print(f'A nova idade deve ser maior que a anterior')

colaborador1 = Pessoa('Ana', 36, 'Assistente Jr')
colaborador2 = Pessoa('Joao', 45, 'Dev Jr')

colaborador1.informacoes()
colaborador1.promover('Assistente Pleno')
colaborador1.atualizar_idade(37)
