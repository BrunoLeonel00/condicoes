# aumento de salario, pergunte o salario e reajuste com base no salario atual
print('{:=^40}'.format('\033[1;34mNOVO SISTEMA DE AUMENTO\033[m'))
print('''\033[1;35msalarios até R$ 280 terão  20% de aumento
salarios entre R$ 280 e R$700 terão  15% de aumento
salarios entre R$ 700 e R$ 1500 terão 10% de aumento
salarios de R$ 1500 terão 5%.\033[m''')
salario = float(input('Digite seu salario atual: R$ '))
print('\nSeu salario antes do reajuste era de R$\033[1;37m{:.2f}\033[m'.format(salario))
#AUMENTO DOS SALARIOS
if salario <= 280:
    aumento = salario + (20 / 100 * salario)
    print('O percentual de aumento aplicado foi de 20% (R$\033[1;37m{:.2f}\033[m)'.format(20 / 100 * salario))
    print('E o seu novo salario após o aumento é de R$\033[1;37m{:.2f}\033[m'.format(aumento))
elif salario <= 700:
    aumento = salario + (15 / 100 * salario)
    print('O percentual de aumento aplicado foi de 15% (R$\033[1;37m{:.2f}\033[m'.format(15 / 100 * salario))
    print('E o seu novo salário após o aumento é de R%\033[1;37m{:.2f}\033[m'.format(aumento))
elif salario < 1500:
    aumento = salario + (10 / 100 * salario)
    print('O percentual de aumento aplicado foi de 10% (R$\033[1;37m{:.2f}\033[m)'.format(10 / 100 * salario))
    print(' E o seu novo salário após o aumento é de R$\033[1;37m{:.2f}\033[m'.format(aumento))
elif salario >= 1500:
    aumento = salario + (5 / 100 * salario)
    print('O percentual de aumento aplicado foi de 5% (R$\033[1;37m{:.2f}\033[m'.format(5 / 100 * 100))
    print('E o seu novo salário após o aumneto é de R$\033[1;37m{:.2f}\033[m'.format(aumento))


