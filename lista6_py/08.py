#script que solicite a digitação do primeiro nome do usuário e então preencha e exiba uma matriz 4 x 4 contendo as letras do nome informado (uma letra em cada posição) sequencialmente, repetindo o nome até preencher toda a planilha.

print("-="*20)
nome = input("- Digite seu nome: ").upper()
matriz_nome = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cont = 0

for l in range(0,4):
    for c in range(0,4):
        if cont == len(nome):
            cont = 0
            matriz_nome[l][c] = nome[cont]
            cont += 1
        else:
            matriz_nome[l][c] = nome[cont]
            cont += 1

print("-"*40)
print(f'{"Matriz ":^40}')
print("-"*40)

for l in range(0,4):
    print("   ", end='')
    for c in range(0,4):
        print(f"[{matriz_nome[l][c]:^5}] ", end='')
    print()

print("-="*20)