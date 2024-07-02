#script que solicite ao usuário que digite uma palavra qualquer. Em seguida, gere uma matriz quadrada de ordem 4 e preencha os elementos dessa matriz, na sequência, com as letras que compõem a palavra digitada. Terminado o preenchimento dos elementos com a palavra, o script deve então completar os demais elementos da matriz com o caracter ‘X’.

print("-="*20)
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cont = 0

palavra = input(f"- Digite uma palavra: ").upper()

for l in range(0,4):
    for c in range(0,4):
        if cont == len(palavra):
            matriz[l][c] = "X"
        else:
            matriz[l][c] = palavra[cont]
            cont += 1

print("-"*40)
print(f'{"Matriz ":^40}')
print("-"*40)

for l in range(0,4):
    print("    ", end='')
    for c in range(0,4):
        print(f"[{matriz[l][c]:^5}] ", end='')
    print()
print("-="*20)
