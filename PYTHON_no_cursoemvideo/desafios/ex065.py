contador = 0
ultimo = 1
soma = 0
media = 0
maior = 0
menor = 0
print('Digite 0 para saber a média')
while ultimo != 0:
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor and n != 0:
            menor = n
    if n == 0:
        contador += -1
        media = soma / contador
        print(f'A média dos números digitados foi {media:.2f}')
        print(f'O maior número digitado foi {maior}')
        print(f'O menor número digitado foi {menor}')
        resposta = input('Deseja continuar?(s/n) ').upper()
        if resposta == 'N':
            print('Obrigado por testar o programa')
            ultimo = 0