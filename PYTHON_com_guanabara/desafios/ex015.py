dias = int( input('Quantos dias o carro foi alugado: '))
km = float( input('Quantos km rodados: '))

preco = (dias * 60) + (km * 0.15)

print('O preço  a pagar será de R${:.2f}'.format(preco))