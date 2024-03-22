num = int(input('Informe um número: '))
print('Analisando o número {}'. format(num))

unidade = num % 10
print('Unidade: {}'.format(unidade))

dezena = (num % 100 - unidade)
print('Dezena: {:.0f}'.format(dezena / 10))

centena = (num % 1000)
print('Centena: {:.0f}'.format(centena / 100))

milhar = (num % 10000)
print('Milhar: {:.0f}'.format(milhar / 1000))
