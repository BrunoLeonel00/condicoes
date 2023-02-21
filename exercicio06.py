#Faca um programa que receba dois numeros e imprima o maior, caso os dois numeros forem iguas, imprima "numeros iguais"
n1 = int(input('Digite um numero:'))
n2 = int(input('digite mais um numero:'))
if n1 == n2:
    print('numeros iguais')
if n1 > n2:
    print('o maior numero entre eles é {}'.format(n1))
else:
    print('o maior numero entre eles é {}'.format(n2))
