metros = float(input('Digíte a quantidade de métros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A medida de {} metros equivale á:'.format(metros))
print('{} Km'.format(km))
print('{} Hm'.format(hm))
print('{} Dam'.format(dam))
print('{} Dm'.format(dm))
print('{} Cm'.format(cm))
print('{} Mm'.format(mm))