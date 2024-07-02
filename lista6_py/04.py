#script que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 e, ao final, exiba e informe a localização (linha e coluna) do elemento de maior valor da planilha. 

m = [[0,0,0],[0,0,0],[0,0,0]]

print("-="*20)
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"- Digite o valor em [{l}][{c}]: "))

maior = m[0][0]
for l in range(0,3):
    for c in range(0,3):
        if m[l][c] > maior:
            maior = m[l][c]
            pos_lin = l
            pos_col = c
print("-"*40)
print(f'{"Matriz 3x3":^40}')
print("-"*40)

for l in range(0,3):
    print("   ", end='')
    for c in range(0,3):
        print(f"[{m[l][c]:^5}] ", end='')
    print()
print("-"*40)

print(f"O maior elemento da matriz é {maior}!")
print(f"Está na posição [{pos_lin}][{pos_col}]")
print("-="*20)