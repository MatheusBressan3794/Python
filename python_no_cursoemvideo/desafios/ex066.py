contador = s = 0
print('Digite 999 para parar.')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador += 1
    s += n
print(f'Você digitou {contador} números')
print(f'A soma deles foi de {s}')