num = int(input('Digite um número: ').strip())
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades: {}'.format(u))
print('Desenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))
