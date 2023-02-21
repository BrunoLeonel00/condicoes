#fazendo um jogo de impar e par
from random import randint
from time import sleep
print('Bem vindo ao jogo')
computador = randint(1, 10)
opcao = str(input('Voce escolhe IMPAR ou PAR?')).strip().lower()
player = int(input('Digite um Número de 1 a 10:'))
resultado = (computador + player) % 2
print('-=-' * 10)
print('o jogador escolheu {}'.format(player))
print('o compuador escolheu {}'.format(computador))
print('-=-' * 10)
if opcao == 'par': # se o jogador escolher par como opçao
    if resultado == 0:
        print('JOGADOR vence!')
    elif resultado != 0:
        print('COMPUTADOR vence')

elif opcao == 'impar': # se o jogador escolger impar
    if resultado != 0:
        print('JOGADOR vence')
    elif resultado == 0:
        print('COMPUTADOR vence')


