user = input('digite o usuario:   ')
password = input('digite a senha:   ')

login_valido = user == 'Admin' and password == '123admin'

print(f'Login Permitido: {login_valido}')
