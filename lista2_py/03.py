#script que solicita duas notas, calcula e mostra a média aritmética
print("-="*20)
n1 = float(input("- Primeira nota: "))
n2 = float(input("- Segunda nota: "))
n3 = float(input("- Terceira nota: "))
soma = n1 + n2 + n3
media = soma/3
if media >= 7:
    print(f"O aluno foi aprovado com média {media:.1f}")
else:
    print(f"O aluno foi reprovado com média {media:.1f}")
print("-="*20)
