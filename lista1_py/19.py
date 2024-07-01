#script que calcula a media final do aluno
print("-"*35)
print(f'{"Calculador de media final":^35}')
print("-"*35)
n1 = float(input("- Nota 1: "))
n2 = float(input("- Nota 2: "))
n3 = float(input("- Nota 3: "))
n4 = float(input("- Nota 4: "))
soma = (n1*2) + (n2*2) + (n3*3) + (n4*3)
media = soma / 10
print(f"A média final do aluno foi de {media:.1f}")
print("-"*35)
