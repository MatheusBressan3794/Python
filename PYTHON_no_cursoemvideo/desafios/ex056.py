maiorm = 0
idades = 0
moças = 0
velho = ''
for p in range(1, 5):
    sexo = input('Qual o sexo da {}º pessoa (M ou F): '.format(p)).upper()
    idade = int(input('Idade da pessoa: '))
    nome = input('Nome da pessoa: ').title()
    idades += idade
    if p == 1 and sexo == 'M':  # Se for homem a primeira idade já vai ser a maior
        maiorm = idade
        velho = nome  
    if idade > maiorm:# Vai analizar as outras idades e colocar a maior na variavel
            maiorm = idade
            velho = nome
    if sexo == 'F':
        if idade <= 20:
            moças += 1
media = idades / 4
print('A média de idade do grupo foi de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorm, velho))
print('E tem {} mulheres abaixo dos 20 anos'.format(moças))
