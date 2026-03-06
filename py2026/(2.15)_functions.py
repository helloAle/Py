# ========================================================

#               15 -> funções reutilizaveis

# ========================================================

#  bloco de construção onde escrevemos uma vez e utilizamos varias

# def saudacao(nome, idade):
#   print(f'Olá! {nome}! Você tem {idade} anos de idade!')
  
# saudacao('ale', 24)
# saudacao('maria', 25)

# --------------------------

# def somar(num1, num2):
#   return num1 + num2

# total = somar(4, 5)
# print(f'O resultado da soma de é de {total}')

# --------------------------

def calcular_desconto(preco, porcentagem):
  return preco - (preco * porcentagem / 100)

valor_final = calcular_desconto(100, 20)
print(f'O valor final com desconto é de R${valor_final:.2f}')
