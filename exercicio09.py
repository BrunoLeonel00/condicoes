#'''Faça um programa que receba a altura e o sexo de uma pessoa, e calcule e mostre seu peso ideal
# ultilizando a formula (HOMEM: 72.7*H)- 58  (Mulher: 62.1 * H)- 44,7'''
genero = str(input('indique seu genero?')).strip().title()
altura = float(input('qual a sua altura?'))
peso1 = float(input('indique seu peso atual:kg '))
if genero == 'Masculino':
    peso = (72.7 * altura) - 58
    print('seu peso ideial é igual a {:.2f}'.format(peso))
    if peso < peso1:
        print('Voce precisa emagrecer {:.2f}Kg para se manter saudavel'.format(peso1 - peso))
if genero == 'Feminino':
    peso = (62.1 * altura) - 44.7
    print('seu peso ideal é igual a {:.2f}'.format(peso))
    if peso < peso1:
        print('voce precisa emagrecer {:.2f} para se manter saudavel'.format(peso1 - peso))
