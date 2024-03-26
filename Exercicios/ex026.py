nome = str(input("Digite uma frase: ")).strip().lower()

if "a" in nome.lower():
    print("A letra A aparece {} vezes na frase.".format(nome.count("a")))
    print("A primeira letra A aparecer na posição {}".format(nome.find("a") + 1 ))
    print("A ultima letra A aparecer na posição {}".format(nome.rfind("a") + 1))
else:
    print('a frase não possui nenhuma letra "a"')
