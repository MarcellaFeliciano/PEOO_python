#script que solicita ao usuário a digitação de 10 números e ao final exibe-os no formato de lista mas em ordem inversa.

lista = []
lista_reverse = []
print("-="*20)
for i in range(1,11):
    n = int(input(f"- Digite o {i}° valor da lista: "))
    lista.append(n)
print("-"*40)
for n in range(len(lista)-1,-1,-1):
    lista_reverse.append(lista[n])
print(f'{"Lista invertida":^40}')
print("-"*40)
print(f' {lista_reverse}')
print("-="*20)

    