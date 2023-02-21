#calculadora basica
num1 = float(input('Digite um número:'))
num2 = float(input('Digite mais um número:'))
print('''Escolha uma das opções:
[ 1 ] soma
[ 2 ] subtração
[ 3 ] multiplicação
[ 4 ] divizao''')
op = int(input('qual a sua escolha?'))
if op == 1:
    print('A soma de {} e {} é igual a {:.2f}'.format(num1, num2, num1 + num2))
elif op == 2:
    print('A subtração de {} e {} é igual a {:.2f}'.format(num1, num2, num1 - num2))
elif op == 3:
    print(' A multiplicaçao de {} e {} é igual a {:.2f}1'.format(num1, num2, num1 * num2))
elif op == 4:
    print('a divizao de {} e {} é igual a {:.2f}'.format(num1, num2, num1 / num2))


