#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença que existe entre ambos
num1 = int(input('digite um numero:'))
num2 = int(input('digite mais um numero:'))
if num1 >= num2:
    diferença = num1 - num2
    print('O maior número digitado foi {}, e a diferença entre eles é {}'.format(num1, diferença))
else:
    diferença = num2 - num1
    print('o maior número digitado é {}, e a diferença entre eles é igual a {}'.format(num2, diferença))
