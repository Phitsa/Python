nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu texto...')
print('seu nome em maiúsculas é ', nome.upper())
print('seu nome em minúsculas é ', nome.lower())
print('seu nome tem ao todo {} letras'.format( len(nome) - nome.count(' ')))

primeiro_nome = nome.split()
print('seu primeiro nome é ', primeiro_nome[0])

if nome.find(' ') >= 1:
    print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
else:
    print('seu primeiro nome tem {} letras'. format(len(nome)))
