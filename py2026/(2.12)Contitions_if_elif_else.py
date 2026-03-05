# =================== 12 -> condições ======================

op = int(input('BEM VINDO, SELECIONE O SISTEMA:  \n1) login \n2) não sei \n             '))
if op == 1:
  user = input('digite o seu usuario: ')
  password = input('digite sua senha: ')

  if user == 'admin' and password == 'admin':
    print('login ok')
  else:
    print(':(')
elif op == 2:
  print('nem eu')
else:
  print('Comando não conhecindo')
