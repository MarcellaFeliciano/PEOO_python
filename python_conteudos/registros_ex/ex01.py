# Registro tem um indice e adicionar valores/lista a essa chave.
# Dicionarios de listas

agenda = {}
print("-="*20)
while True:
    nome = input(f"- Nome: (para sair - PARE) ")
    if nome.upper() == "PARE":
        break
    telefone = int(input("Número de telefone: "))
    agenda[nome] = telefone
print(agenda)
print("-="*20)

cidadao = {}

for i in range(0,3):
    nome = input(f"Nome: ")
    telefone = int(input("Telefone: "))
    email = input(f"Email: ")

    #se não existir ele cria, e se existir ele substitui! 
    cidadao.update({'nome': nome})
    cidadao.update ({'telefone': telefone})
    cidadao.update({'email': email})
print(cidadao['nome'])

