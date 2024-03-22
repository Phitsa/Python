import random

a = str(input('Digite o nome do Aluno '))
b = str(input('Digite o nome do Aluno '))
c = str(input('Digite o nome do Aluno '))
d = str(input('Digite o nome do Aluno '))

print('o Aluno escolhido foi {}'.format(random.choice([a,b,c,d])))