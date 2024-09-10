s = 'denovo'
while s == 'denovo':
    s = input('Qual o seu sexo?(M/F): ').upper()
    if s == 'M' or s == 'F':
        s = 'acabou'
    else:
        print('Essa gênero não existe')
        s = 'denovo'
print(f'Sexo {s} registrado com sucesso')
print('Obrigado por responder')