
try:
    while True print('Hello world')

except SyntaxError as erro:
    print('- Nome do arquivo inesistente!')
    print(f'Erro: {erro}')
    print(f'Classe do erro: {type(erro)}')

except IndentationError: 
    print("ERROOO")

except Exception:
    print("isso")

#exception of exception - exceção da exceção

# Tendo em vista que dois erros ocorrem simutaneamente, independente da exceção ele irá parar o codigo com tanto erro de syntax como de indentação!

# explicar o que aconteceu? tratar o erro de forma diferente, porque mesmo ao indentificar o erro e 
# a escessão, ao chamar o erro e a classe mesmo assim não funciona!