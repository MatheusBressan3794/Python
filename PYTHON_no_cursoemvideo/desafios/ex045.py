from random import randint
print('ESCOLHA UMA OPÇÃO:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
user = int(input('Qual a opção escolhida? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Você escolheu {}'.format(itens[user]))
print('E o computador escolheu {}'.format(itens[computador]))
if computador == 0:
    if user == 0:
        print('Empate')
    elif user == 1:
        print('Você VENCEU, parabéns!')
    elif user == 2:
        print('Computador wins')
    else:
        print('Jogada INVALIDA')

elif computador == 1:
    if user == 0:
        print('Computador wins')
    elif user == 1:
        print('Empate')
    elif user == 2:
        print('Você VENCEU, parabéns!')
    else:
        print('Jogada INVALIDA')

elif computador == 2:
    if user == 0:
        print('Você VENCEU, parabéns!')
    elif user == 1:
        print('Computador wins')
    elif user == 2:
        print('Empate')
    else:
        print('Jogada INVALIDA')