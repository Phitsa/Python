largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))

print('Sua parede tem a dimensão de ({} x {}) e sua área é de {}m²'.format(largura,altura,largura * altura))
print('Considerando que para cada 2m² de parede você precisa de 1 litro de tinta\npara pintar toda a parede você precisará de {}l de tinta'.format((largura * altura) / 2))