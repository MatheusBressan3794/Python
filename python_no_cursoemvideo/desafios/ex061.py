primeiro = int(input('Digite o primeiro termo de uma PA: '))
razão = int(input('Digite a razão dela: '))
décimo = primeiro + (10 - 1) * razão
print('Os 10 primeiros termos são:')
while primeiro != décimo + razão:
    print(primeiro, end=' -> ')
    primeiro += razão
print('Fim')