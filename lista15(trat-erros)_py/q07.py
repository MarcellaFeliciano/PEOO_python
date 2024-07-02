from colorama import Fore
contatos = []
print("-"*50)
print(f'{"Agenda de Contatos":^50}')
print("-"*50)
while True:
    situacao = 'nome_invalido'
    nome = input(" - Digite um nome: ('fim' = parar) ")
    if nome == 'fim':
        break
    else:
        try:
            if 'X' in nome.upper():
                raise Exception('Não pode ter X no nome!')
            else:
                situacao = 'nome_valido'

        except Exception as erro:
            print(f"{Fore.RED}Erro: {erro}{Fore.WHITE}") 

        if situacao == 'nome_valido':
            while True:
                telefone = input(" - Digite o telefone: ")
                try:
                    if telefone.isnumeric():
                        situacao = 'numero_valido'
                    else:
                        raise Exception('O telefone só pode ter números!')

                except Exception as erro:
                    print(f"{Fore.RED}Erro: {erro}{Fore.WHITE}") 

                if situacao == 'numero_valido':
                    registro = {nome:telefone}
                    contatos.append(registro)

                    break
print("-"*50)
print(f'{"A G E N D A":^50}')
print("-"*50)

for i in contatos:
    print("  ", end='')
    for k in i.keys():
        print(f" Nome - {k}")
    print("  ", end='')
    for v in i.values():
        print(f" Telefone - {v}")
    print()

print("-"*50)
        
