salario = float( input('Qual é seu salário atual? '))

aumento = salario * 0.15
nsalario = salario + aumento

print('Com o aumento de 15% no seu salario que foi de {:.2f} reais, seu novo salário será de {:.2f} reais'.format(aumento, nsalario))