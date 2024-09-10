casa = float(input('Qual o valor da casa? R$'))
salario1 = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
salario2 = salario1 * 0.30

if prestacao >= salario2:
    print(f'O emprestimo será concedido, pois a prestação de R${prestacao:.2f} em {anos} excede o valor de 30% de seu salário.')
else:
    print(f'O emprestimo NÃO será concedido, pois a prestação de R${prestacao:.2f} em {anos} é menor do que 30% de seu salário.')
