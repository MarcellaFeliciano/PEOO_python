#script que solicite a digitação dos elementos (letras quaisquer do alfabeto) de uma matriz 3 x 3 e ao final exiba a matriz, insira as letras da diagonal principal em uma lista e, finalmente, exiba essa lista.

print("-="*20)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
principal = []
cont = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = input(f"- Valor (letra do alfabeto) em [{l}][{c}]: ").upper()
        
for l in range(0,3):
    for c in range(0,3):
        if l == c:
            principal.append(matriz[l][c])


print("-"*40)
print(f'{"Matriz ":^40}')
print("-"*40)

for l in range(0,3):
    print("       ", end='')
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}] ", end='')
    print()
    
print("-"*40)
print(f"- Diagonal principal: {principal}")
print("-="*20)