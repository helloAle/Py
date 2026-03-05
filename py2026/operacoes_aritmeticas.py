# ===============

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print(f'adição:           {num1} + {num2} = {num1 + num2}')
print(f'subtração:        {num1} - {num2} = {num1 - num2}')
print(f'multiplicação:    {num1} * {num2} = {num1 * num2}')
print(f'divisão:          {num1} / {num2} = {num1 / num2}')

print(f'divisão inteira:  {num1} // {num2} = {num1 // num2}')
print(f'resto da divisão: {num1} % {num2} = {num1 % num2}')
print(f'potencia:         {num1} ** {num2} = {num1 ** num2}')

# desconto 
valor = int(input("Digite o valor do produto: "))
desc = int(input("Digite o desconto: "))
print(f'desconto:         o produto que custava {valor} passou a custar {valor - ((valor / 100)* desc)} com o desconto de {desc}% aplicado')
