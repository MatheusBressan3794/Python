primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
mais = 0
termo = 10
contador = 1
resposta = ''
print('OS 10 primeiros termos são:')
while resposta != 'N':
    termo += mais
    while contador <= termo:
        print(primeiro, end=' -> ')
        primeiro += razao
        contador += 1
    print('Pausa')
    resposta = str(input('Você deseja saber mais termos (S/N)? ').upper().strip())
    if resposta == 'S':
        mais = int(input('Quantos termos a mais você quer saber? '))
print('Ok, obrigado por testar o programa.')
print(f'Foi mostrado {termo} termos')