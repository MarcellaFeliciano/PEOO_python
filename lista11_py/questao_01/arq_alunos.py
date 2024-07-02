from classes_aluno import *
import os

print("-="*20)
print(f'{"Informe as informações do aluno":^40}')
print("-"*40)
matricula = input("- Matricula: ")
nome = input("- Nome: ")
turma = input("- Turma: ")
nota_1 = float(input("- Valor da 1° nota: "))
nota_2 = float(input("- Valor da 2° nota: "))
print("-="*20)

boletim = Notas(nota_1,nota_2)

aluno = Aluno(matricula=matricula, nome=nome, turma=turma, boletim=boletim)
os.system('cls')
print()
print("-="*15)
print(f'{"Dados do Aluno":^30}')
print("-"*30)
print(f" Matricula - {aluno.matricula}")
print(f" Nome - {aluno.nome}")
print(f' Turma - {aluno.turma}')
print('- '*15)
print(f" Nota 1 - {aluno.boletim.nota1}")
print(f" Nota 2 - {aluno.boletim.nota2}")
print(f" Média - {aluno.boletim.media}")
print("-="*15)