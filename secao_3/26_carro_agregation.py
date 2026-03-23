
class Motor:
  def __init__(self, marca, potencia):
    self.marca = marca
    self.potencia = potencia

class Carro:
  def __init__(self):
    self.motores = []

  def adicionar_motor(self, motor):
    self.motores.append(motor) # .append vai adicionar um item a lista

  def listar_motores(self):
    for motor in self.motores:
      print(f'Marca: {motor.marca} - {motor.potencia} cavalos de potencia')

# criando os motores

motor_v6 = Motor('ford', 300)
motor_v8 = Motor('Ferrari', 650)
motor_v12 = Motor('Lamborghini', 950)

# criar o carro e adincionar o motor nele

carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)

# Listar os motores
carro.listar_motores()
  
