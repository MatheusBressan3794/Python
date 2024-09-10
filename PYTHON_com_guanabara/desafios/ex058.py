from random import randint
print('-=-' * 20)
print('O programa vai sortear um número de 0 a 10, tente adivinhar')
print('-=-' * 20)
sorteado = randint(0, 10)
n = 11
contador = 0
n = int(input('Digite um número: '))
while n != sorteado:
    n = int(input('Errou, tente novamente outro: '))
    contador += 1
print('Parabéns, você acertou em {} tentativas'.format(contador))