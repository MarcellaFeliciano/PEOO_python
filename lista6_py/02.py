 #script que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 e, ao final, exiba quantos e quais valores inseridos são maiores que 10.

m = [[0,0,0],[0,0,0],[0,0,0]]
cont = 0
maior_10 = []
print("-="*20)

for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f"- Digite o valor em [{l}][{c}]: "))

for l in range(0,3):
    for c in range(0,3):
        if m[l][c] > 10:
            cont += 1
            maior_10.append(m[l][c])

print("-"*40)
print(f'{"Matriz":^40}')
print("-"*40)
for l in range(0,3):
    print("   ", end='')
    for c in range(0,3):
        print(f"[{m[l][c]:^5}] ", end='')
    print()

print("-"*40)
print(f"Foram digitados {cont} valores maiores que 10!")
print(f"- Os números são : {maior_10}")
print("-="*20)