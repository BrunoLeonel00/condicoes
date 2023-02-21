#'''Faça um programa que pergunte em que turno voce estude, M- matutino, V- verpertino, N- noturno, e
# imprima a menssagem, boa dia, boa tarde e boa noite'''
print('''Olá, em qual periodo voce estuda?
[ M ] Matutino
[ V ] Verpetino
[ N ] noturno''')
turno = str(input('Digite a letra correspondente aqui:')).strip().lower()
if turno == 'm':
    print('\033[1;34mBOM DIA\033[m, tenha uma otima aula, e um otimo dia')
elif turno == 'v':
    print('\033[1;36mBOA TARDE\033[m, tenha uma otima aula, sem preguiça')
elif turno == 'n':
    print('\033[1;32mBOA NOITE\033[m, tenha uma otima aula, e tome cuidado ao voltar.')
else:
    print('\033[1;31m MENSSAGEM INVALIDA\033[m')
