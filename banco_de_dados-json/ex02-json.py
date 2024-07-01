import requests, json
# o metodo json pega arquivos/dados da web
from colorama import Fore

cnpj = input("Digite o cnpj para consutar: ")
# 10877412001210
consulta = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}')

# print(consulta.status_code) # mostra se funciona ou não ( 200 - okay / 404 - erro)


if consulta.status_code != 200:
    print(f'{Fore.RED}Cnpj Inválido! {Fore.WHITE}')

else:
    print("","-"*30,f"{Fore.GREEN}")
    print(f"{'Cnpj Valido!' :^30}")
    print(f'{Fore.WHITE}',"-"*30)
    
    print(f'- Razão Social: {consulta.json()["razao_social"]}')
    print(f'- Nome Fantasia: {consulta.json()["nome_fantasia"]}')
    print(f'- Municipio: {consulta.json()["municipio"]}')