# Script que receba registros inseridos por um usuário com os campos: aluno (string) e media (float) de 0 a 100.
aprovados = dict()
reprovados = dict()
print("-="*20)
print(f"{'Registro dos alunos':^40}")
print("-"*40)
while True:
    aluno = input("Nome do aluno: ('pare') ")
    if aluno.upper() == "PARE":
        break
    media = float(input("Média do aluno: (0 á 100) "))
    campus = [aluno, media]
    if media >= 60:
        aprovados[aluno] = campus
    else:
        reprovados[aluno] = campus

print("-"*40)
print(f'{"Alunos aprovados":^40}')
print("-"*40)
for n in aprovados.values():
    print(f" - Nome: {n[0]} ~ Média: {n[1]}")

print()
print("-"*40)
print(f'{"Alunos reprovados":^40}')
print("-"*40)
for n in reprovados.values():
    print(f" - Nome: {n[0]} ~ Média: {n[1]}")

print("-"*40)
