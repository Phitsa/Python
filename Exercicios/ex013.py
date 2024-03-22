preço = float(input('Qual sé o Salário do Funcionário? R$'))
desconto = float(input('Qual o valor do aumento (em porcentagem)? '))
print('O Funcionário ganhva R${:.2f}, depois do aumento de {:.0f} ele passou a ganhar R${:.2f}'.format(preço,desconto,(preço + desconto * (preço / 100))))