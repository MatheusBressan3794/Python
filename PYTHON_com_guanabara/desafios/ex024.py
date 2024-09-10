cidade = str( input('Informe o nome da sua cidade: ')).strip().lower()
separa = cidade.split()
print('O nome da sua cidade começa com Santo: {}'.format('santo' in separa [0]))
