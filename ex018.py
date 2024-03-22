import math
angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o Seno de {:.2f}\nO ângulo de {} tem o Cosseno de {:.2f}\nO ângulo de {} tem a Tangente de {:.2f}'.format(angulo,math.sin(angulo * 3.14/180),angulo,math.cos(angulo * 3.14/180),angulo,math.tan(angulo * 3.14/180)))