#o objetivo aqui é ver se o nome da cidade que você colocar começa com santo
cidade = str(input('Em que cidade você nasceu? ')).strip()

cidade1 = cidade.lower()
print(bool(cidade1[:5] == 'santo'))
