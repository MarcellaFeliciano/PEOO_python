 # não é inrteressante ele parar com alguma exceção do nome e ainda pedi ro numero de telefone
contatos = []
while True:
    nome = input("Nome ou fim: ")
    if nome == 'fim':
        break
    else:
        try:
            if 'x' in nome or 'X' in nome:
                raise Exception('Não pode ter X no nome!')
        except Exception as erro:
            print("Erro!") 

telefone = input("Digite o telefone: ")
registro = {nome:telefone}
contatos.append(registro)

print(contatos)