#Essa biblioteca importa varias funções de matematica#
import math
num = int( input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Ou poder ser feito assim para economizar memória #

from math import sqrt
num = int( input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))