n1 = float(input('Digíte um número: '))
n2 = float(input('Digíte outro número: '))

soma = n1 + n2
sub = n1 - n2
mut = n1 * n2
div = n1 / n2
pot = n1 ** n2
dint = n1 // n2
sob = n1 % n2

print('A soma de {} e {} é: {}'.format(n1, n2, soma))
print('A subtração de {} menos {} é: {}'.format(n1, n2, sub))
print('A mutiplicação de {} e {} é: {}'.format(n1, n2, mut))
print('A divisão de {} pelo {} é: {}'.format(n1, n2, div))
print('A potência de {} elevado a {} é: {}'.format(n1, n2, pot))
print('A divisão inteira de {} pelo {} é: {}'.format(n1, n2, dint))
print('A sobra da divisão entre {} e {} é: {}'.format(n1, n2, sob))
