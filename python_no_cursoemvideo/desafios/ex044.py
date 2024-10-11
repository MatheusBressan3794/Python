print('LOJA DO MATHEUS')
preço = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
op = input('Qual a opção: ')
if op == '1':
    print('Desconto de 10%')
    desconto = preço * 0.10
    np = preço - desconto
    print('A compra ficou R${:.2f}'.format(np))
elif op == '2':
    print('Desconto de 5%')
    desconto = preço * 0.05
    np = preço - desconto
    print('A compra ficou R${:.2f}'.format(np))
elif op == '3':
    np = preço / 2
    print('Você irá pagar 2 parcelas de R${:.2f} sem juros'.format(np))
elif op == '4':
    vezes = int(input('Quantas vezes? '))
    print('Com 20% de JUROS')
    total = (preço * 0.20) + preço
    np = total / vezes
    print('A compra ficara R${:.2f} e as percelas serão de R${:.2f}'.format(total, np))