f = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(f.count('a')))
print('Ela aparece a primeira vez na possição {} e a última vez na possição {}'.format(f.find('a') + 1, f.rfind('a') + 1))