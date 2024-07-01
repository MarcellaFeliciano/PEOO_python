while True:  
    agenda.open('agenda.txt', 'a')
    nome = input("Insira o nome: ('sair' par afinalizar!) ").upper()
    if nome == "SAIR":
        break
    telefone = input(f'Insira o telefone de {nome.capitalize()}: ')
    agenda.write(f"{nome} : {telefone}\n")
