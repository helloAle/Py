#=========================seção 2=============================

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print(nome)
print(idade)


nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

# sem f-string
print('Olá', nome + ', Você tem', idade, 'anos de idade' )

# com f-string
print(f'Olá {nome}, Você tem {idade} anos de idade' )

print(f'Olá {nome}, daqui 5 anos você terá {idade + 5} anos de idade')
