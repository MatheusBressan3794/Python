n = int(input('Digite um número inteiro: '))
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Escolha sua opção: '))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)))
else:
    print('Não tem essa opção')