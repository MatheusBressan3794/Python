n = int(input('Digite um número: '))
print('-' * 12)
for c in range(1, 11):
    r = c * n
    print('{} x {} = {}'.format(c, n, r)) # Não precisa somar +1 ao c 
print('-' * 12)