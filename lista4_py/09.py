#script que solicita ao usuário a digitação de um número inteiro (maior que 1000). Em seguida, transforme o número para string, 
#inverta o número totalmente (ex: 2345 vira 5432), transforme novamente para inteiro, some com 1000 e exiba o resultado.

print("-="*25)
numero = int(input("- Digite um número positivo maior que 1000: "))
while numero <= 1000:
    numero = int(input("- Digite um número positivo maior que 1000: "))
n = str(numero)
num = ""
for i in range(len(n)-1, -1, -1):
    num += n[i]
inteiro = int(num)
print("-"*50)
print(f" O resutado é {inteiro + 1000}!")
print("-="*25)