dias = int(input('Quantos dias alugados? '))
kilometros = float(input('Quantos Kilometros rodados? ')) 
print('O total a pagar é de R${:.2f}'.format(dias * 60 + kilometros * 0.15))