# api - intermediação enttre a inteface e o programa
# como pegar o valor e a chave que pegue o valor  dos dados         


import requests
import json
arquivo = requests.get('https://api.github.com')
#arquivo json dogithub

#pegoo arquivo json pego a chave e pego o valor do que eu procuro
print(arquivo.json()['emogis_url'])