#script que solicite ao usuário que digite um número e exiba “Palíndromo” caso o número digitado seja um palíndromo e “Não é palíndromo” caso não seja.
print("-"*35)
num = input("- Digite um número: ")
print("-"*35)
inverso = ""
for i in range(len(num)-1, -1, -1):
    inverso += num[i]
if num == inverso:
    print(f"O número {num} é um palíndromo!")
else:
    print(f"O número {num} não é um palíndromo!")
print("-"*35)