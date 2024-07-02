#script que, inicialmente, define duas matrizes quadradas de ordem 5 (de nomes ‘vogais’ e ‘consoantes’). Em seguida o script armazena em uma LISTA o SEU PRIMEIRO NOME (cada letra como um elemento da lista) construída a partir das letras das duas matrizes definidas inicialmente.

print("-="*20)
lista_nome = []
vogais = [["A",0,0,0,0],[0,"E",0,0,0],[0,0,"I",0,0],[0,0,0,"O",0],[0,0,0,0,"U"]]
consoantes = [["B","C","D","F","G"],["H","J","K","L","M"],["N","P","Q","R","S"],["T","V","W","X","Y"],["Z",0,0,0,0]]
cont = 0
nome = input("- Digite seu nome: ").upper()
print("-"*40)


while cont < len(nome):
    resp = "nao"

    for l in range(0,5):
        if cont == len(nome):
            break
        for c in range(0,5):
            if vogais[l][c] == nome[cont]:
                lista_nome.append(vogais[l][c])
                print(f"- {nome[cont]} = Matriz vogais - posição ({l},{c})")
                cont += 1
                resp == "sim"
                break
                
                
    if resp == "nao":
        for l in range(0,5):
            if cont == len(nome):
                break
            for c in range(0,5):
                if consoantes[l][c] == nome[cont]:
                    lista_nome.append(consoantes[l][c])
                    print(f"- {nome[cont]} = Matriz consoantes - posição ({l},{c})")
                    cont += 1
                    break
                    
print("-"*40)
print(lista_nome)
print("-="*20)
