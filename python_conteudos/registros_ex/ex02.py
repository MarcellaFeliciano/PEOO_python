alunos = {
    1234: "João",
    2222: 'Maria'
}

alunos[4444] = "Zé"
alunos.update({3333: "Chico"})
alunos.update({3333: "Marcella"})
print(type(alunos))
print(type(alunos[1234]))
print(alunos)
print("-"*30)
for a in alunos.items():
    print(a)

print("-"*30)

for a,b in alunos.items():
    print(f"Chave: {a} / Valor: {b}")

print("-"*30)
print(f"Numeros de alunos: {len(alunos)}")
print("-"*30)

organizados = sorted(alunos.items())

print(organizados)

del alunos[1234]
alunos.pop(3333)

print(alunos)