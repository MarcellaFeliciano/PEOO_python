#while True:
    #arq = open('amigos.txt', 'a')
    #arq.write(input(f"- Nome do amigo: "))
    #arq.close()
    #saida = input("-> ").upper()
    #if saida == "SAIR":
     #   break

#-------------------------
amigo = " "
while True:
    arq = open('amigos.txt', 'a')
    amigo = input("Nome do amigo: ")
    arq.write((f"{amigo} \n"))
    saida = input("-> ").upper()
    if saida == "SAIR":
        break
arq.close()