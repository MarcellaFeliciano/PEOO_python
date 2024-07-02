from colorama import Fore
senha = ''
while True:
    try:
        print("-"*40)
        senha = input(' -> Digite uma senha: ')
        if len(senha) < 8:
            raise Exception('Senha menor que 8 caracteres')
        elif senha == 'internacional':
            raise Exception('Senha não pode ser internacional')
        else:
            break
    except Exception as erro:
        print(f' {Fore.RED} Erro! {erro}!{Fore.WHITE}')

print(f'{Fore.GREEN}- Senha criada com sucesso:{Fore.WHITE} {senha}!')