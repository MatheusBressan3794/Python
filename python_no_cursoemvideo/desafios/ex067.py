cont = r = 0
while True:
    cont = 0
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        print('Números negativos não são aceitos')
        break
    print('-=-' * 20)
    while cont != 11:
        r = n * cont
        print(f'{n} x {cont} = {r}')
        cont += 1
    print('-=-' * 20)