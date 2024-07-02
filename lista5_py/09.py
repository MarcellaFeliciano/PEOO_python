#script que solicite ao usuário que digite uma frase (sem acentos) e ao final exiba: Quantos espaços em branco existem no texto, e Quantas vezes aparecem as vogais a, e, i, o, u.
print("-="*30)
frase = input("- Digite uma frase: ").lower()
print("-"*60)
branco = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for n in frase:
    if n == " ":
        branco += 1
    if n == "a":
        a += 1
    elif n == "e":
        e += 1
    elif n == "i":
        i += 1
    elif n == "o":
        o += 1
    elif n == "u":
        u += 1
print(f"-> A frase '{frase}' tem:")
print(f"{branco} espaços em branco!")
print(f"Vogais -  {a} A's / {e} E's / {i} I's / {o} O's / {u} U's")

print("-="*30)
