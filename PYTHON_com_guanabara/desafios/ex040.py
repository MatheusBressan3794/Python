n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua Média foi de {:.2f}'.format(media))
if media < 5:
    print('O aluno está REPROVADO')
elif media >= 5 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')