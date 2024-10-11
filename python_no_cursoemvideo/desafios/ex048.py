print('A soma entre todos os números impares, mutiplos de 3 de 1 a 500 é:')
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print(s)