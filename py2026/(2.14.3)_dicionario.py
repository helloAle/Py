#               14.3 -> dicionario

# usuario = {
#     'nome': 'ale',
#     'idade': 24,
#     'departamento': 'TI'
# }

# usuario['idade'] = 25

# print(usuario)


aluno = {
    'nome': input('Nome do aluno: '),
    'idade': input('Idade do aluno: '),
    'nota': input('Nota do aluno: ')
}

print(f'{aluno['nome']} tem {aluno['idade']} anos de idade e tirou {aluno['nota']} na média')
