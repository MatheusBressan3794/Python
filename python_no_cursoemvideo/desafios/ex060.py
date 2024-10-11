n = int(input('Digite um número para calcular seu fatorial: '))
mut = n
print('Seu fatorial é:')
print('{}! = '.format(n), end='')
while n != 1:
    print(n, end=' x ')
    n -= 1
    mut *= n
print('1 = ', end='')
print(mut)