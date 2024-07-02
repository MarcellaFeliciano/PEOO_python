#script que solicita ao usuário a digitação de 10 números e ao final exibe-os em ordem crescente.
lista = []
lista_crescente = []
print("-="*20)
for i in range(1,6):
    n = int(input(f"- Digite o {i}° valor da lista: "))
    lista.append(n)
lista.sort()
print("-"*40)
print(f"{'Lista em ordem crescente':^40}")
print("-"*40)
print(f" {lista}")
print("-="*20)
