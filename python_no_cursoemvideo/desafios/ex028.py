from random import randint
print('-=-' * 20)
print('O programa vai sortear um numero de 0 a 5. Tente adivinhar')
print('-=-' * 20)
numero = int(input('Digite um número: '))
sorteado = randint(0, 5) # O computador vai sortear um número de 0 a 5
if numero == sorteado:
    print('Parabéns!!!, você acertou o número!')
else:
    print(f'Você errou, o número era {sorteado}, tente outra vez')