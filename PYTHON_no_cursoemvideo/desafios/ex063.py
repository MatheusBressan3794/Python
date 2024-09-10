termo_desejado = int(input('Quantos termos você deseja? '))
t1 = 1
t2 = 1
t = 1
contador = 0
print('1 -> ', end='')
while contador != termo_desejado -1:
    print(t, end=' -> ')
    t = t1 + t2
    t1 = t2
    t2 = t
    contador += 1
print('Fim')