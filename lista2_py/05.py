#script que solicita 3 valores digitados A, B e C e informa se pode formar um triangulo
print("-="*30)
a = int(input("- Digite o 1° valor: "))
b = int(input("- Digite o 2° valor: "))
c = int(input("- Digite o 3° valor: "))

if a<(b+c) and b<(a+c) and c<(a+b):
    print("Os valores de A B e C podem ser os lados de um triangulo!")
else:
    print("Os valores não podem ser os lados de um triangulo!")
print("-="*30)