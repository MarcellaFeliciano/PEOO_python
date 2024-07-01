import requests, json

consulta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

print(consulta)

#print(consulta.json())

#print(consulta.json()['USDBRL'])
data_cotacao = consulta.json(['USDBRL']['bid'])
valor = consulta.json()['USDBRL']['bid']

print(f"O valor da {data_cotacao} é de {valor}")