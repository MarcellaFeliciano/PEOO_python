#scrpt onde o usuário insere um número inteiro positivo e recebe como resultado o fatorial desse número.
print("-="*20)
print(f'{"Calculo de fatorial":^40}')
print("-"*40)
num = int(input("- Digite um número inteiro positivo: "))
print("-"*40)
n = num
fat = num

print(f"{num}!= {num} x ",end='')
while n != 1:
    n -= 1
    if n == 1:
        fat = fat * n
        print(f"{n} = {fat}")
    else:
        fat = fat * n
        print(f"{n} x ", end='')
        
print(f"O fatorial de {num} é {fat}")
print("-="*20)