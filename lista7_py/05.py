# Script que peça para o usuário entrar com registros de alunos com as seguintes informações: matrícula (inteiro), nome (string), nota1 (float de 0 a 100) e nota2 (float de 0 a 100).

registro = {}
cont = 0
while True:
    cont+=1
    print("-"*30)
    print(f"  Registro do {cont}° aluno")
    print("-"*30)
    matricula = int(input(" Matricula (0 para parar): "))
    if matricula == 0:
        break
    nome = input(" Nome: ")
    nota1 = float(input(" ~ 1° nota: "))
    nota2 = float(input(" ~ 2° nota: "))
    campus = [nome, nota1, nota2]
    registro[matricula] = campus

print("-="*30)
print(f'{"R E G I S T R O":^60}')
print("-"*60)
print(f"- Alunos matriculados: {len(registro)}")
print()
print(f"- Nome dos alunos: ", end='')
for n in registro.values():
    print(f"{n[0]} / ", end='')
print()
print()
soma_1 = 0
print("- Média das notas da 1° unidade: ", end='')
for n in registro.values():
    soma_1 += n[1]
media = soma_1 / len(registro)
print(f'{media:.2f}')
print()
soma_2 = 0
print("- Média das notas da 2° unidade: ", end='')
for n in registro.values():
    soma_2 += n[2]
media = soma_2 / len(registro)
print(f'{media:.2f}')
print()
print(f"- A média final da turma é: ", end='')
media_final = (soma_1 + soma_2) / (len(registro)*2)
print(f"{media_final:.2f}")
print()
print("- Lista de alunos aprovados: ", end='')

for v in registro.values():
    soma = v[1] + v[2]
    media = soma / 2
    if media >= 60:
        print(f"{v[0]}, ", end='')
print()
print("-"*60)

