#script que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 e calcule e exiba a soma dos elementos da diagonal secundária dessa matriz.


m_1 = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0

print("-="*20)
for l in range(0,3):
    for c in range(0,3):
        m_1[l][c] = int(input(f"- Valor da 1° matriz em [{l}][{c}] : "))

cont = 2
for l in range(0,3):
    for c in range(0,3):  
        if c == cont:
            soma += m_1[l][c]
            cont -= 1

print("-"*40)
print(f'{"Matriz 1":^40}')
print("-"*40)

for l in range(0,3):
    print("       ", end='')
    for c in range(0,3):
        print(f"[{m_1[l][c]:^5}] ", end='')
    print()
    
print("-"*40)
print(f"A soma da diagonal secondaria é {soma}!")
print("-="*20)
