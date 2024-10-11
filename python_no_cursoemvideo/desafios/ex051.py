primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
décimo = primeiro + (10 - 1) * razão
print('Os 10 primeiros termos são:')
for c in range(primeiro, décimo, + razão):
    print(c, end=' -> ')
print('Acabou')