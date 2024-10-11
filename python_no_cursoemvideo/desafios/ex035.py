m1 = float(input('Digite uma medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))
if (m1 + m2 > m3) and (m1 + m3 > m2) and (m2 + m3 > m1):
    print('É possivel formar um triângulo com essas medidas!')
else:
    print('Não é possivel formar um triângulo com essas medidas')