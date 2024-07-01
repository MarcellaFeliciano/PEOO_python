#script que solicita seu nome e em seguida em que turno você estuda
print("-="*20)
nome = input("- Digite seu nome: ")
turno = input("- Digite seu turno: (M/V) ").upper().strip()[0]
if turno == "M":
    print(f" Bom dia, {nome}!")
elif turno == "V":
    print(f" Boa tarde, {nome}!")
else:
    print(f" Erro encontrado {nome}!")
print("-="*20)
