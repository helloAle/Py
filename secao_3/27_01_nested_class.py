# criar a classe main

class Computador:
  def __init__(self, modelo, gpu_nome, gpu_memoria):
    self.modelo = modelo
    self.gpu_nome = gpu_nome
    self.gpu = self.GPU(gpu_nome, gpu_memoria) # bem aqui ocorre a interação (self.gpu chama self.GPU)
  
  def mostrar_configuracao(self):
    print(f'Computador: {self.modelo}')
    self.gpu.mostrar_gpu()

  class GPU: # NESTED CLASS
    def __init__(self, nome, memoria_gb):
      self.nome = nome
      self.memoria_gb = memoria_gb

    def mostrar_gpu(self):
      print(f'GPU: {self.nome} {self.memoria_gb}')

#  UTILIZAÇÃO

# pc1 = Computador('modelo', placa[nome], mamoria[memoria_gb])
pc1 = Computador('Dell XPS', 'NVIDIA RTX 4090', 24)
pc1.mostrar_configuracao()
