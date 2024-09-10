nome = str(input('Digite seu nome completo: ')).strip()

print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('E {} tem {} letras'.format(separa[0], len(separa[0])))