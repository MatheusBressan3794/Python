n1 = int(input('Digite um número: '))
n2 = int(input('O segundo número: '))
n3 = int(input('O terceiro número: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 <n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor número digitado foi {menor}')
print(f'E o maior número é {maior}')
""" Colocando maior e menor = n1, eu eliminei um if."""
