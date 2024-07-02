#script que solicita ao usuário a digitação de 5 números inteiros e os armazena em uma lista. Ao final imprime os 5 números seguidos de sua posição na lista.
lista = []
print("-="*15)
for i in range(1,6):
    n = int(input(f"Digite o {i}° número da lista: "))
    lista.append(n)
print("-="*15)
print(f'{"Número e posição":^30}')
print("-"*30)
for i, n in enumerate(lista):
    print(f"  Número {n} na posição {i}.")

print("-="*15)

