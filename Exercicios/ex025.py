nome = str(input("Qual é o seu nome completo? ")).strip()

nomel = nome.lower()
print(nomel.find("silva"))

if nomel.find("silva") >= 0:
    print("seu nome tem Silva")
else:
    print("seu nome não tem silva")

print("Seu nome tem Silva? {}".format("silva" in nome.lower()))
