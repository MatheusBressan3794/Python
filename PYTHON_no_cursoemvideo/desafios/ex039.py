from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
idade = atual - ano
print('Você tem ou vai fazer {} anos de idade'.format(idade))
if idade > 18:
    alistamento = ano + 18
    print('Seu alistamento foi em {}'.format(alistamento))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
else:
    alistamento = ano + 18
    print('Você devera se alistar em {}'.format(alistamento))