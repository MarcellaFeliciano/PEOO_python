import requests, json
# o metodo json pega arquivos/dados da web
from colorama import Fore
# pegar o values de citiees e colocar em uma lista e perguntar se cityesta in lisa

ddd = input("Digite o ddd para consutar: ")



consulta = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{ddd}')


if consulta.status_code != 200:
    print(f'{Fore.RED}DDD Inválido! {Fore.WHITE}')

else:
    print("","-"*30,f"{Fore.GREEN}")
    print(f"{'DDD Valido!' :^30}")
    print(f'{Fore.WHITE}',"-"*30)

    # cidade = input('Qual a cidade a consular? ')
    #teste = consulta.json()['cities']
    #print(type(teste)) -> list
    
    cidade = input('Qual a cidade a consular? ').upper()

    if cidade in consulta.json()['cities']:
        print(f"{cidade} faz parte do DDD {ddd}!")

    else:
        print(f"{cidade} não faz parte do DDD {ddd}!")