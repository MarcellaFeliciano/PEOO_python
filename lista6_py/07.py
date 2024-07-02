#script que solicite a digitação dos elementos (números inteiros) de duas matrizes 3 x 3 e ao final gere e exiba, além das duas matrizes digitadas, uma terceira matriz com os maiores valores de cada posição das matrizes lidas.

m_1 = [[0,0,0],[0,0,0],[0,0,0]]
m_2 = [[0,0,0],[0,0,0],[0,0,0]]
m_3 = [[0,0,0],[0,0,0],[0,0,0]]

print("-="*20)
for l in range(0,3):
    for c in range(0,3):
        m_1[l][c] = int(input(f"- Valor da 1° matriz em [{l}][{c}] : "))

print("-"*40)
for l in range(0,3):
    for c in range(0,3):
        m_2[l][c] = int(input(f"- Valor da 2° matriz em [{l}][{c}] : "))

print("-"*40)
print("Calculando a 3° Matriz...")

for l in range(0,3):
    for c in range(0,3):
        if m_1[l][c] > m_2[l][c]:
            m_3[l][c] = m_1[l][c]
        else:
            m_3[l][c] = m_2[l][c]



print("-"*40)
print(f'{"Matriz 1":^40}')
print("-"*40)

for l in range(0,3):
    print("       ", end='')
    for c in range(0,3):
        print(f"[{m_1[l][c]:^5}] ", end='')
    print()
print("-"*40)


print("-"*40)
print(f'{"Matriz 2":^40}')
print("-"*40)

for l in range(0,3):
    print("       ", end='')
    for c in range(0,3):
        print(f"[{m_2[l][c]:^5}] ", end='')
    print()


print("-"*40)
print(f'{"Matriz 3":^40}')
print("-"*40)

for l in range(0,3):
    print("       ", end='')
    for c in range(0,3):
        print(f"[{m_3[l][c]:^5}] ", end='')
    print()
print("-"*40)