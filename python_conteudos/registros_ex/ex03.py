# Registro tem um indice e adicionar valores/lista a essa chave.
# Dicionarios de listas

alunos = {111 : ['Marcella Pereira', 'marcella.p@gmail.com', '98778-6355'], 
        222 : ['Chico Lopes', 'chico@gmail.com', '9888-6355']}
dados_alunos = []
print("-="*25)
busca = int(input("- Digite a matricula do aluno: "))
print("-"*50)
if busca in alunos.keys():
    dados_alunos = alunos[busca]
    print(f"     ~ Dados do aluno com Matricula ({busca}) ~")
    print(f" Aluno - {dados_alunos[0]}")
    print(f" Email - {dados_alunos[1]}")
    print(f" Telefone - {dados_alunos[2]}")
else:
    print(" Não existe aluno cadastrado com a matricula informada!")

print("-="*25)
    