nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0].title()))
print('E seu último nome é: {}'.format(n[len(n) - 1].title()))