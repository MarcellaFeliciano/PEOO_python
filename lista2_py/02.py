#script que solicita tres números e mostra-os em ordem crescente
print("-="*20)
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))
print("-"*40)
print("Ordem crescente: ", end='')
if n1<n2 and n1<n3 and n2<n3:
    print(f"{n1}, {n2}, {n3}")
elif n1<n2 and n1<n3 and n3<n2:
    print(f"{n1}, {n3}, {n2}")
elif n2<n1 and n2<n3 and n1<n3:
    print(f"{n2}, {n1}, {n3}")
elif n2<n1 and n2<n3 and n3<n1:
    print(f"{n2}, {n3}, {n1}")
elif n3<n1 and n3<n2 and n1<n2:
    print(f"{n3}, {n1}, {n2}")
elif n3<n1 and n3<n2 and n2<n1:
    print(f"{n3}, {n2}, {n1}")
else:
    pritn("Erro em ordenar!")
print("-="*20)