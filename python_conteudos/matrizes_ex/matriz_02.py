m1 = []
print("-="*20)
lin = int(input("Digite a quant. de linhas da matriz: "))
col = int(input("Digite a quant. de colunas da matriz: "))
for i in range(0,lin):
    linha = [0]*col
    m1.append(linha)

print("-"*30)
for l in range(0,lin):
    for c in range(0,col):
        m1[l][c] = int(input(f"- Digite o valor em [{l}][{c}]: "))
print("-"*30)

print(f'{"Matriz 1":^30}')
for l in range(0,lin):
    print("   ", end='')
    for c in range(0,col):
        print(f"[{m1[l][c]:^5}] ", end='')
    print()
print("-"*30)

menor = 0
for l in range(0,lin):
    for c in range(0,col):
        if l == 0 and c == 0:
            menor = m1[0][0]
        else:
            if m1[l][c] < menor:
                menor = m1[l][c]

m2 = []
for l in range(0,lin):
    m2.append([0]*col)

for l in range(0,lin):
    for c in range(0,col):
        m2[l][c] = m1[l][c] * menor

print(f'{"Matriz 2":^30}')
for l in range(0,lin):
    print(f"   ", end='')
    for c in range(0,col):
        print(f"[{m2[l][c]:^5}]", end='')
    print()
print("-="*20)
