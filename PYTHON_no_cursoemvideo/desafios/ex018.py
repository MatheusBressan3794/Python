import math
ang = int( input('Digite um ângulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O seno de {} é {:.3f}'.format(ang, seno))
print('O cosseno de {} é {:.3f}'.format(ang, cosseno))
print('A tangente de {} é {:.3f}'.format(ang, tangente))