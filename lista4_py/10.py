#script que solicita ao usuário que digite números inteiros indefinidamente e, ao final, digite zero para finalizar a entrada de dados.
# Os números devem ser inseridos em uma lista à medida em que forem sendo digitados pelo usuário. Ao final transforme todos os números 
# em um único número (ex: [12, 4, 32, 12] = 1243212) e exiba o resultado.
print("-="*15)
print(" Insira valores e pare no (0)")
print("-="*15)
lista = []
total = ""
n = -1
while n != 0:
    n = int(input("- Digite um número: "))
    if n != 0:
        lista.append(n)
for i in lista:
    total += str(i)

print("-"*30)
print(f" O resutado é {total}!")
print("-="*15)