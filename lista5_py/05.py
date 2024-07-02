#script que solicite ao usuário que digite uma frase (onde pode utilizar pontos, vírgulas, interrogações, etc… à vontade) e então informe o número de palavras contidas na frase inserida.
print("-"*35)
frase = input("Digite uma frase: ")
for i in range(0, len(frase)-1):
    if frase[i] == "." or frase[i] == "!" or frase[i] == "?" or frase[i] == ",":
        frase = frase.replace(frase[i], "")

print(f"A frase tem {len(frase.split())} palavras!")
print("-"*35)

