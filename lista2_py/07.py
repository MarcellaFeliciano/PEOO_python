#script que solicita um número inteiro e se for par calcula o quadrado e se for impar calcula o cubo
print("-="*15)
num = int(input("- Digite um número inteiro: "))
if num%2 == 0:
    quad = num**2
    print(f" O quadrado de {num} é {quad}")
else: 
    cubo = num**3
    print(f" O cubo de {num} é {cubo}")
print("-="*15)
