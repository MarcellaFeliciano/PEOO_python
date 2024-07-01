m1 = []
print("-="*25)
lin = int(input("Digite a quant. de linhas da matriz: "))
col = int(input("Digite a quant. de colunas da matriz: "))
for i in range(0,lin):
    linha = [0]*col
    m1.append(linha)

print("-"*30)
for l in range(0,lin):
    for c in range(0,col):
        m1[l][c] = int(input(f"- Digite o valor em [{l}][{c}]: "))
print("-"*(col*10))

for l in range(0,lin):
    print("  ", end='')
    for c in range(0,col):
        print(f"[{m1[l][c]:^5}] ", end='')
    print()
print("-"*(col*10))

m_t = []
for i in range(0,col):
    linha = [0]*lin
    m_t.append(linha)

for l in range(0,lin):
    for c in range(0,col):
        m_t[c][l] = (m1[l][c])

for l in range(0,col):
    print("  ", end='')
    for c in range(0,lin):
        print(f"[{m_t[l][c]:^5}] ", end='')
    print()
print("-="*25)

print("- O maior elemento na matriz é: ", end='')

maior = 0
for l in range(0,lin):
    for c in range(0,col):
        if l == 0 and c == 0:
            maior = m1[0][0]
        else:
            if m1[l][c] > maior:
                maior = m1[l][c]
print(maior)
print("-="*25)