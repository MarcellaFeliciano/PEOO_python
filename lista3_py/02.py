#script onde o usuário insere números quaisquer e recebe como resultado a soma de todos os números pares entre os números informados.
print("-="*20)
print(f" Insira valores e para parar digite 0!")
print("-"*40)
num = 1
soma = 0
while num != 0:
    num = float(input("- Digite um número: "))
    if num%2 == 0:
        soma += num
print("-"*40)
print(f"A soma dos números pares é {soma}")
print("-="*20)


