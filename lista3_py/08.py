#script que recebe números positivos e conta quantos deles estão nos seguintes intervalos: [1-25], [26-50], [51-75] e [76-100].
print("-"*40)
num = 1
inter_1 = inter_2 = inter_3 = inter_4 = 0
while num != 0:
    num = int(input("- Digite um número positivo: "))
    if num >= 1 and num <= 25:
        inter_1 += 1
    elif num >= 26 and num <= 50:
        inter_2 += 1
    elif num >= 51 and num <= 75:
        inter_3 += 1
    elif num >= 76 and num <=100:
        inter_4 += 1
print("-"*40)
print("Quantidade de numeros em cada intervalo:")
print("-"*40)
print(f" [1 - 25] ~ {inter_1} números.")
print(f" [26 - 50] ~ {inter_2} números.")
print(f" [51 - 75] ~ {inter_3} números.")
print(f" [76 - 100] ~ {inter_4} números.")
print("-"*40)