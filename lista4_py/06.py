#script que solicita ao usuário a digitação de 5 números, armazena-os em uma lista e, em seguida, solicita ao usuário que digite um número e consuta se está na lista ou nao.
lista = []
print("-="*20)
for i in range(1,6):
    n = int(input(f"- Digite o {i}° número: "))
    lista.append(n)
print("-"*40)
num = int(input(" - Digite um valor: "))
if num in lista:
    print(f" O número {num} está na lista!")
else:
    print(f" O número {num} não está na lista!")
print("-="*20)


        

