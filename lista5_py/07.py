#script que solicite ao usuário que digite uma frase e exiba “Palíndromo” caso a frase seja um palíndromo e “Não é palíndromo” caso não seja.
print("-"*35)
frase = input("Digite uma frase: ").lower()
inverso = ""
for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]
if frase == inverso:
    print(f"A frase {frase} é um palíndromo!")
else:
    print(f"A frase {frase} não é um palíndromo!")
print("-"*35)
