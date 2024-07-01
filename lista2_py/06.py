#script que solicita um número inteiro e diz se este é par ou ímpar
print("-="*15)
num = int(input("- Digite um número inteiro: "))
if num%2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")
print("-="*15)