idade = int(input('Qual a sua idade? '))
nome = str(input('Qual o seu nome? ')).strip
if idade >= 18:
    print(f'{nome} você é maior de idade')
else:
    print(f'{nome} você é menor de idade')