velocidade = int(input('Qual a velocidade do carro em km? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'O carro foi multado em {multa} reais. Pois estava em uma velocidade maior que 80 Km/h.')
else:
    print('Velocidade OK, dirija com segurança.')