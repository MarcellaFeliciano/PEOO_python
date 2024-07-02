#O script recebe do usuário quantos números ele desejar (e digita zero para finalizar). O script então calcula a soma de todos os números digitados e a média aritmética deles.
soma = 0
cont = 0
num = 1
print("-="*20)
print(f"Insira valores e para parar digite 0!")
print("-"*40)
while num != 0:
    num = float(input("- Digite um número: "))
    soma += num
    if num!=0:
        cont += 1
media = soma/contoo
print("-"*40)
print(f"A soma dos números é {soma}")
print(f"A média dos números foi {media}")
print("-="*20)
