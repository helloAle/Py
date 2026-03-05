# CALCULAR QUANTOS DIAS UM PRODUTO DURARIA SE UMA PESSOA USAR X PORÇÕES POR DIA

produto = input('Insira o nome do seu produto:    ')
quantidade = int(input('Insira a quantidade em gramas do seu produto:   '))
gasto = int(input(f'quanto você consome diariamente deste produto?    '))
dias = 0

# basico
d = quantidade / gasto
print(f'Seu produto acaba em {d:.0f} dias')

# com while
while quantidade > 0:
  quantidade = quantidade - gasto
  dias = dias + 1
print(f'Seu produto acaba em {dias} dias')
