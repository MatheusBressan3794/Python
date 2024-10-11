preco = float( input('Informe o valor do produto: '))

desconto = preco * 0.05
npreco = preco - desconto

print('Com o desconto de 5% que é {:.2f} reais, o valor do produto será: {:.2f}'.format(desconto, npreco))