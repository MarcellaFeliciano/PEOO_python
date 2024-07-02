#script que define um número inteiro (de 1 a 100) no próprio script como sendo o ‘número sorteado’
print("-"*45)
sorteado = int(input("-> O número escolhido do sorteio é: "))
num = 0
cont = 0
print("-"*45)
print(f'{"Tente adivinhar o número sorteado!":^45}')
print("-"*45)
while num != sorteado:
    cont += 1
    num = int(input(f"- {cont}° palpite: " ))
    if num != sorteado:
        print(' Errou. você não está com sorte!')
    else:
        print("-"*45)
        print(" Parabéns! Você acertou o número sorteado!")
        print("-"*45)
