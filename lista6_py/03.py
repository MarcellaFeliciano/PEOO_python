#script que exiba uma matriz 4 x 4 onde o valor de cada elemento da matriz é igual a multiplicação dos seus índices (posição linha x posição coluna). 

matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("-="*20)
for l in range(0,4):
    for c in range(0,4):
        matriz[l][c] = l * c

print(f'{"Matriz 4x4":^40}')
print("-"*40)

for l in range(0,4):
    print("   ", end='')
    for c in range(0,4):
        print(f"[{matriz[l][c]:^5}] ", end='')
    print()
print("-="*20)