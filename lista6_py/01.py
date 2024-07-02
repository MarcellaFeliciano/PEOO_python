 #script que peça para o usuário entrar com o número de linhas (m), colunas (n) e os elementos (números inteiros) de uma matriz A e depois calcule e mostre a matriz B, tal que B é igual à transposta de A (AT).

m = []
print("-="*20)
lin = int(input("Digite o número de linhas da matriz: "))
col = int(input("Digite o número de colunas da matriz: "))

for l in range(0,lin):
    linha = [0]*col
    m.append(linha)

print("-"*40)
for l in range(0,lin):
    for c in range(0,col):
        m[l][c] = int(input(f"- Digite o valor em [{l}][{c}]: "))
print("-"*40)
print(f'{"Matriz":^40}')
print("-"*40)
for l in range(0,lin):
    print("   ", end='')
    for c in range(0,col):
        print(f"[{m[l][c]:^5}] ", end='')
    print()


m_t = []
for l in range(0,col):
    linha = [0]*lin
    m_t.append(linha)

for l in range(0,lin):
    for c in range(0,col):
        m_t[c][l] = (m[l][c])


print("-"*40)
print(f'{"Matriz Transposta":^40}')
print("-"*40)
for l in range(0,col):
    print("   ", end='')
    for c in range(0,lin):
        print(f"[{m_t[l][c]:^5}] ", end='')
    print()
print("-="*20)