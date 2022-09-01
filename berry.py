
from re import match

print("Calculadora ^-^")
print('1-soma\n2-subtração\n3-multiplicação\n4-divisão')
print("selecione um numero: ")
op = input()
if op == '1':
    print("Soma")
elif op == '2':
    print("Subtração")
elif op == '3':
    print("Multiplicação")
elif op == '4':
    print("Divisão")
else:
    print('problema')



# match op:
#     case 1:
#         print('Soma')
#     case 2:
#         print('Subtração')
#     case 3:
#         print('Multiplicação')
#     case 4:
#         print('Divisão')