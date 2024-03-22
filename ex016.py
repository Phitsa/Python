from math import floor
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}'.format(num,floor(num))) # eu
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))     # guanabara
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))       # guanabara Melhor!