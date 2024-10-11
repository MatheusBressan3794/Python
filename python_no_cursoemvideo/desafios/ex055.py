maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: # O maior peso digitado vai para a variavel maior
            maior = peso
        if peso < menor: # O menor peso digitado vai para a variavel menor
            menor = peso
print('O MAIOR peso foi de {} kg'.format(maior))
print('O MENOR peso foi de {} kg'.format(menor))