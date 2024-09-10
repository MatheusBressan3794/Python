viagem = int(input('Qual a distância em km da sua viagem? '))
if viagem <= 200:
    preço = viagem * 0.50 
else:
    preço = viagem * 0.45
print(f'O preço da viagem é de R${preço:.2f}')