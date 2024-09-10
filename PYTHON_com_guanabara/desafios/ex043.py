peso = float(input('Qual o seu peso (Kg)? '))
altura = float(input('Qual a sua altura (m)? '))
imc = peso / (altura ** 2) 
print('Seu IMC foi de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal, Parabéns')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso, faça uma diéta')
elif imc > 30 and imc < 40:
    print('Você está com obesidade, TOME CUIDADO!')
elif imc > 40:
    print('Você está com obesidade mórbida, CUIDADO!')