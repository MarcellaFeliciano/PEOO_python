# Faça uma agenda utilizando um script Python para armazenar 5 registros (nome/telefone) informados pelo usuário em uma lista de dicionários. Em seguida, exiba os 5 registros (um por linha).

agenda = dict()

for i in range(1,6):
    print("-"*30)
    print(f"   Registro da {i}° pessoa")
    print("-"*30)
    nome = input("- Nome: ")
    telefone = int(input("- Telefone: "))
    registro = [nome, telefone]
    agenda[i] = registro
print()
print("-="*25)  
print(f'{"A G E N D A":^50}')
print("-"*50)
for n,r in agenda.items():
    print(f" {n}° Registro - Nome: {r[0]} / Telefone: {r[1]}")
    print("-"*50)