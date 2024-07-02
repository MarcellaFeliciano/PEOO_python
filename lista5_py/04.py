#script Python que solicite ao usuário que informe uma string e então informe quantas vezes cada letra/caractere que a compõe aparece na string. Não diferencie maiúsculas e minúsculas.
print("-"*30)
string = input("Digite um texto: ").lower()
vezes = []
letra = []
cont = 0
for i in string:
    if i not in letra:
        cont += 1
        letra.append(i)
        vezes.append(string.count(i))

print("-"*30)
for i in range(0,cont):
    print(f" - Letra {letra[i].upper()} aparece {vezes[i]} vezes!")
print("-"*30)