soma = 0
contar = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        contar += 1
print(' A soma de todos dos {} números pares digitados é {}'.format(contar, soma))