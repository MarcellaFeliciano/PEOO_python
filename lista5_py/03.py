#script que solicite ao usuário que informe duas strings e então verifique se a segunda string informada encontra-se dentro da primeira. Se sim, exiba a posição do início da segunda string dentro da primeira.
print("-"*30)
s1 = input("Digite um texto: ")
s2 = input("Digite outro texto: ")
if s2 in s1:
    print("-"*30)
    print("- O texto 2 está no texto 1!")
    print(f"Inicia na posição {s1.index(s2[0])}")
else:
    print("-"*30)
    print("- O texto 2 não está no texto 1!")
print("-"*30)
