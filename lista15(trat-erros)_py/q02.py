print("-"*35)
print('   Listagem dos nomes do arquivo')
print("-"*35)
linha = 1
try:      # nome do arquivo é nome.txt!
    arquivo = open('nomes.txt','r')
    for nome in arquivo:
        print(f'Linha[{linha}] -> {nome}', end='')
        linha+=1
except Exception as erro:
    print('- Nome do arquivo inesistente!')
    print(f'Erro: {erro}')
    print(f'Classe do erro: {type(erro)}')

