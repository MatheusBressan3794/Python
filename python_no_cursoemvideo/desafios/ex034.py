salario = float(input('Qual o seu salário: '))
if salario >= 1250:
    porcentagem = salario * 0.10
    aumento = salario + porcentagem
    print(f'O seu aumento será de R${porcentagem:.2f}') 
    print(f'Seu salário será de R${aumento:.2f}')
else:
    porcentagem = salario * 0.15
    aumento = salario + porcentagem
    print(f'O seu aumento será de R${porcentagem:.2f}') 
    print(f'Seu salário será de R${aumento:.2f}')