#script que solicite ao usuário que preencha duas listas com 5 elementos cada. Gere então e exiba uma terceira lista contendo os elementos das duas listas informadas sem elementos repetidos.

print("-="*25)
print(f'{"Atribua valores as listas":^60}')
lista1 = []
lista2 = []
lista3 = []
for i in range(0,2):
    print("-"*50)
    for n in range(1,6):
        if i == 0:
            num = int(input(f"- {n}° valor da lista 1: "))
            lista1.append(num)
        else:
            num = int(input(f"- {n}° valor da lista 2: "))
            lista2.append(num)
for n in lista1:
    if n not in lista3:
        lista3.append(n)
for n in lista2:
    if n not in lista3:
        lista3.append(n)
        
print("-"*50)
print(f" Lista 1 -> {lista1}")
print(f" Lista 2 -> {lista2}")
print(f" Lista 3 -> {lista3}")
print("-="*25)
