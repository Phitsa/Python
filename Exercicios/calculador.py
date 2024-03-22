from calculador2 import calcula

textos = {
    1: 'o resultado da soma é {}!',
    2: 'o resultado da subtração é {}!',
    3: 'o resultado da Media é {}!'   
}

def programa():
    print('Escolha uma função')
    print('Lista:')
    print('soma      = 1')
    print('subtração = 2')
    print('media     = 3')

    opcao = int(input('\nDigite o numero equivalente a função escolhida:  '))

    num1 = int(input('Digite o primeiro valor '))
    num2 = int(input('Digite o segundo  valor '))

    if opcao != 1 and opcao != 2 and opcao != 3:
        print('\nVocé não seguiu as regras!\n')
        return True
    
    print(textos[opcao].format(calcula(num1, num2, opcao)))
    return False