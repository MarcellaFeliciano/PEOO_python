mat = []
print("-="*15)
for l in range(0,3):
    linha = []
    for c in range(0,3):
        linha.append(input(f"Digite o valor de [{l}][{c}]: "))
    mat.append(linha)
print("-"*30)
for  l in range(0,3):
    print("       ", end='')
    linha = " | "
    for c in range(0,3):
        linha += mat[l][c] + " "
    linha += "|"
    print(linha)
print("-"*30)
