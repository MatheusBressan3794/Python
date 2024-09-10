from datetime import date
ano = int(input('Informe um ano ou coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto')
else:
    print('Não é um ano bissexto')