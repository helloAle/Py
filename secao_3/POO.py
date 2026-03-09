# programa??o orientada a objetos -> POO
# => organiza??o do c?digo

#classe (Casa):

class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
    
    def mostrar_cor(self):
        print(f'A cor da casa e {self.cor}')

    def mostrar_quartos(self):
        print(f'esta casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'esta casa tem {self.banheiros} banheiros')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'esta casa tem {self.quartos} quartos')

    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')


casa1 = Casa('Azul', 4, 3)
casa2 = Casa('Amarela', 6, 4)

print('\nCasa1: ')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar_casa('vermelho')

print('\nCasa2: ')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()