n = 1
par = impar = 0 # A variavel par e impar tem o valor de 0
print('Digite 0 para terminar')
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
