
try:
    while True print('Hello world')

except SyntaxError as erro:
    print('- Nome do arquivo inesistente!')
    print(f'Erro: {erro}')
    print(f'Classe do erro: {type(erro)}')

#exception of exception - exceção da exção
# explicar o que aconteceu? tartar o errode forma diferente, porque mesmo ao indentificacr oerro e 
# a escessão, ao chmar o erroe  a classe mesmo assim não funciona pq?