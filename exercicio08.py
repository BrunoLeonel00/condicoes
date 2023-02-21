#Leia o salario do usuario e o emprestimo desejado.Se o emprestimo for maior que 20% do salario imprima' emprestimo recusado.
salario = float(input('Digite seu salario:'))
emprestimo = float(input('digite o valor que deseja pegar emprestado:'))
prestaçâo = (20 / 100) * salario
if emprestimo > prestaçâo:
    print(' empretimo recusado')
else:
    print('emprestimo aceito')
