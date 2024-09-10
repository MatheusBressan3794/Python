from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
idade = atual - ano
print('Você tem {} anos e disputa a categoria:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIO')
elif idade >= 26:
    print('MASTER')