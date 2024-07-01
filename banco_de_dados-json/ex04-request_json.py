import requests, json
# o metodo json pega arquivos/dados da web
from colorama import Fore

cep = input("Digite o cep para consutar: ")

consulta = requests.get(f'https://brasilapi.com.br/api/cep/v1/{cep}')

# print(consulta.status_code) # mostra se funciona ou não ( 200 - okay / 404 - erro)


if consulta.status_code != 200:
    print(f'{Fore.RED}Cep Inválido! {Fore.WHITE}')

else:
    print("","-"*30,f"{Fore.GREEN}")
    print(f"{'Cep Valido!' :^30}")
    print(f'{Fore.WHITE}',"-"*30)
    print(f'- Rua: {consulta.json()["street"]}')
    print(f'- Bairro: {consulta.json()["neighborhood"]}')
    print(f'- Cidade: {consulta.json()["city"]}')
    print(f'- Estado: {consulta.json()["state"]}')