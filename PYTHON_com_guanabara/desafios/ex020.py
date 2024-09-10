from random import shuffle
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Segundo: ')
nome3 = input('Terceiro: ')
nome4 = input('Quarto: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))

