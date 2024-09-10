n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Trocar valores')
    print('[ 5 ] Sair do programa')
    opção = int(input('O que você quer fazer: '))
    if opção == 1:
        soma = n1 + n2
        print('-=-' * 20)
        print('A soma deles é {}'.format(soma))
        print('-=-' * 20)
    elif opção == 2:
        mut = n1 * n2
        print('-=-' * 20)
        print('A mutiplicação deles é {}'.format(mut))
        print('-=-' * 20)
    elif opção == 3:
        print('-=-' * 20)
        print('O maior número é:')
        maior = n1
        if n2 > n1:
            maior = n2
        elif n1 == n2:
            maior = n1, n2
            print('Nenhum, pois os dois números são iguais')
        print(maior)
        print('-=-' * 20)
    elif opção == 4:
        print('-=-' * 20)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print('-=-' * 20)
print('Obrigado por ultilizar o programa')