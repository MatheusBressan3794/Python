n = s = 0 # As variáveis n e s valem 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # para/interrompe o programa
    s += n
print(f'A soma de todos os números digitados é {s}')