from random import choice
um = input('Digite o primeiro nome: ')
dois = input('O segundo: ')
tres = input('O terceiro: ')
quatro = input('E o quarto: ')
lista = [um, dois, tres, quatro]
sorteio = choice(lista)
print('O sorteado(a) foi {}'.format(sorteio))