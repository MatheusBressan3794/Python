n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
print('Ele foi divisivel {} vezes'.format(tot))
if tot == 2:
    print(f'{n} é primo')
else:
    print('Não é um número primo')