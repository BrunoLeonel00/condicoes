#"""Faça um programa que leia duas notas de um aluno, verifique se as notas sao validas e exiba na tela a media desse aluno
# para uma nota ser valida tem q estar entre 0 E 10"""
nota1 = float(int(input('Digite sua primeira nota:')))
nota2 = float(int(input('Digite sua segunda nota:')))
if nota1 and nota2 > 0:
    media = (nota1 + nota2) / 2
    print('a sua media é igual a {}'.format(media))
else:
    print('nao é um valor valido')


