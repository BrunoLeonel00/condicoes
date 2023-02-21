#faça um programa que receba um numero inteiro e verifique se ele é par ou impar
num = int(input('Digite um numero:'))
if num % 2 == 0:
    print('O numero {} É PAR'.format(num))
else:
    print('o numero {} É IMPAR'.format(num))
