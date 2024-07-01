m1 = []
print("-="*20)
lin = int(input("Digite a quant. de linhas da matriz: "))
col = int(input("Digite a quant. de colunas da matriz: "))
for i in range(0,lin):
    linha = [0]*col
    m1.append(linha)

print("-"*40)
for l in range(0,lin):
    for c in range(0,col):
        if l == c:
            m1[l][c] = 1

print(f'{"Matriz Indentidade":^40}')
print("-"*40)
for l in range(0,lin):
    print("   ", end='')
    for c in range(0,col):
        print(f"[{m1[l][c]:^5}] ", end='')
    print()
print("-="*20)
