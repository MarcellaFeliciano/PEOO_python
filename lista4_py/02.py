#script que solicita ao usuário a digitação de 5 números inteiros imprime o maior e o menor número digitados seguidos de sua posição na lista
lista = []
print("-="*30)
for i in range(1,6):
    n = int(input(f"- Digite o {i}° valor da lista: "))
    lista.append(n)
for pos,n in enumerate(lista):
    if pos == 0:
        maior = n
        pos_maior = pos
        menor = n
        pos_menor = pos
    else:
        if n > maior:
            maior = n
            pos_maior = pos
        if n < menor:
            menor = n
            pos_menor = pos
print("-"*60)
print(f"O maior número da lista é {maior} na posição {pos_maior + 1}.")
print(f"O menor número da lista é {menor} na posição {pos_menor + 1}.")
print("-="*30)