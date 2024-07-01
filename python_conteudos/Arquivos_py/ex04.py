bla = open('amigos.txt', 'r')
conteudo = bla.readlines()
for i in range(len(conteudo)):
    print(f"Registro {i}: {conteudo[i]}")