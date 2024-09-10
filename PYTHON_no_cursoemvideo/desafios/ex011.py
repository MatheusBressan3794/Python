altura = float( input('Qual é a altura da sua parede? '))
largura = float( input('Qual é a largura da sua parede? '))

metros2 = altura * largura
tinta = metros2 / 2

print('Sua parede tem uma dimenção de {}x{} área de {} m² e precisará de {} litros de tinta.'.format(largura, altura, metros2, tinta))