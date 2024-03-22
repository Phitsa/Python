preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Qual o valor do desconto? '))
print('O produto custava R${:.2f}, na promoção com {:.0f}% de desconto vai custar R${:.2f}'.format(preco,desconto,(preco - desconto * (preco / 100))))