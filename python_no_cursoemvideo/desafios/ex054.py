from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento de {}º pessoa: '.format(c)))
    idade = data - nascimento
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print('Das 7 pessoas {} são de maior de idade e {} são menor de idade'.format(maior, menor))