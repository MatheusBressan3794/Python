f = input('Digite uma frase: ').upper().strip()
palavras = f.split()
junto = ''.join(palavras)# Juntou as palavras e tirou os espaços
inverso = junto[::-1] # Escreveu a palavra de traz pra frente
print(junto,'de tráz pra frente fica ',inverso)
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndrome')