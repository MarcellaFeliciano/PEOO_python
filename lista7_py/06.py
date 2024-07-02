#que crie uma agenda de telefones e e-mails que utilize o ‘nome’ como chave e os demais campos (telefone e e-mails) armazenados como lista no dicionário.
from time import sleep
agenda = {}
while True:
    print("-="*20)
    print(f'{"A G E N D A":^40}')
    print("-="*20)
    print(f"Existem {len(agenda)} contatos cadastrados")
    print("-"*40)
    print("1. Inserir um contato")
    print("2. Consultar um contato")
    print("3. Remover um contato")
    print("4. Listar toda a agenda")
    print("0. Finalizar")
    print("-"*40)
    num = int(input("Digite a opção desejada: "))

    if num == 1:
        print("-"*30)
        print(f'{"Insira o contato":^20}')
        print("-"*30)
        nome = input("Nome: ").lower()
        telefone = int(input("Telefone: "))
        email = input("E-mail: ")
        info = [telefone, email]
        agenda[nome] = info
        print("Adicionando contato...")
        sleep(1)

    elif num == 2:
        print("-"*30)
        busca = input("Insira o nome do contato: ").lower()
        print("Buscando contato...")
        print("-"*30)
        sleep(0.5)
        if busca in agenda.keys():
            n = agenda[busca]
            print(f"Nome: {busca}")
            print(f"Telefone: {n[0]}")
            print(f"E-mail: {n[1]}")
            sleep(2)
        else:
            print(" Contato não encontrado!")
            sleep(0.5)

    elif num == 3:
        print("-"*30)
        busca = input("- Deseja remover o contato de: ").lower()
        if busca in agenda.keys():
            agenda.pop(busca)
            print(f"Removendo o contato de {busca.capitalize()}..")
            sleep(0.5)
        else:
            print("Contato não encontrado!")
            sleep(0.5)

    elif num == 4:
        print("-"*30)
        print(f'{"Agenda Completa":^30}')
        for n,v in agenda.items():
            print("-"*30)
            print(f" Nome: {n}")
            print(f" Telefone: {v[0]}")
            print(f" E-mail: {v[1]}")
            sleep(1)
    elif num == 0:
        print("Fechando agenda...")
        sleep(0.5)
        break

    else:
        print("Erro! Siga o menu!")


