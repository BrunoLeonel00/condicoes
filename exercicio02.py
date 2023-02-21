#leia um numero fornecido pelo usuario,Se esse numero for positivo, mostre a raiz quadrada.Se for negativo, mostre que o numero é invalido
from math import sqrt

num1 = int(input('digite um numero:'))
if num1 >= 0:
    raiz = math.sqrt(num1)
    print('a raiz quadrada de {} é igual a {:.2f}'.format(num1, raiz))
else:
    print('o numero {} é invalido'.format(num1))
