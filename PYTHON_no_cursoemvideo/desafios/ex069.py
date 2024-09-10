dezoito = homem = mulher = cont =0
while True:
    idade = int(input('Idade da pessoa: '))
    sexo = input('Sexo da pessoa [M/F]: ').upper()
    cont += 1
    if idade >= 18:
        dezoito += 1
    elif sexo == 'M':
        homem += 1
    elif idade < 20 and sexo == 'F':
        mulher += 1
    resposta = input('Deseja continuar [S/N]? ').upper()
    if resposta == 'N':
        break
print(f'{cont} cadastrados')
print(f'{dezoito} pessoas tem mais de 18 anos')
print(f'{homem} homens')
print(f'{mulher} tem menos de 20 anos')