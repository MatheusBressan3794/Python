from random import randint
print('Vamos jogar par ou impar')
s = 0
cont = 0
while True:
    n = int(input('Digite um valor: '))
    computador = randint(0, 100)
    s = n + computador
    escolha = input('Par ou Impar [P/I]: ').upper()
    print('-=-' * 20)
    print(f'Você jogou {n} e o computador {computador}. A soma é {s}')
    print('-=-' * 20)
    if escolha == 'P':
        if s % 2 == 0:
            print('Parabéns, você ganhou')
            print('Vamos denovo')
            cont += 1
        else:
            print('Você perdeu')
            break
    if escolha == 'I':
        if s % 2 != 0:
            print('Parabéns, você ganhou')
            print('Vamos denovo')
            cont += 1
        else:
            print('Você perdeu')
            break
if cont > 1:
    print(f'Mas ganhou {cont} vezes seguidas')