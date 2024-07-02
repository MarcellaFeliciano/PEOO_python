
while True:
    nome = input("Insira um nome ('pare' = sair): ")
    if nome =='pare':
        arquivo.close()
        break
    try:
        # - para dar erro = open('D:\nome.txt','a')
        arquivo = open('nome.txt','a') 
        # grava o arquivo no arquivo D / para que de erro ( FileNotFoundError ) pois não cosnegue gravar nesse diretorio
        arquivo.write(nome+'\n') # encerra a linha e pula para baixo
    
    except FileNotFoundError as error:
        print(f'Erro: {error}')
        print(f'Classe do erro:{type(error)}')
        print()