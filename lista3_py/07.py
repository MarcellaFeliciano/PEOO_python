#script onde o usuário insere números quaisquer e recebe como resultado a soma de todos os números pares e números impares
print("-"*40)
print(f" Insira valores e para parar digite 0!")
print("-"*40)
num = 1
soma_par = 0
soma_impar = 0
while num != 0:
    num = float(input("- Digite um número: "))
    if num%2 == 0:
        soma_par += num
    else:
        soma_impar += num
print("-"*40)
print(f"A soma dos números pares é {soma_par}")
print(f"A soma dos números impares é {soma_impar}")
print("-"*40)
