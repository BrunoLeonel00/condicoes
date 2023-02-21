#leia um numero real, se o numero for positivo imprima a raiz quadrada, caso o contrario imprima o numero ao quadrado
from math import sqrt, pow
num1 = float(input('digite um numero:'))
if num1 >= 0:
    raiz = sqrt(num1)
    print('a raiz quadrada de {} é igual a {:.2f}'.format(num1, raiz))
else:
    potencia = pow(num1, 2)
    print(potencia)


