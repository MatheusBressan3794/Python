contador = 0
continua = 'True'
soma = 0
print('O programa vai somar todos os números que você digitar, caso queira parar digite (999)')
while continua == 'True':
    v = float(input('Valor: '))
    contador += 1
    if v == 999:
        contador -= 1
        v = 0
        continua = 'False'
    soma += v
print('A soma dos {} valores digitados é {}'.format(contador, soma))