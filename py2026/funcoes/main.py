# main.py
# devo importar as funções que quero usar do arquivo funcoes.py


# from funcao import saudacao, soma
# import funcao

# funcao.saudacao('ale')
# print(funcao.soma(2, 10))

from funcao import verificar_maioridade
my_age = int(input('Digite a sua idade  '))

if verificar_maioridade(my_age):
    print('Você é maior de idade :)')
else:
    print('Você é menor de idade')