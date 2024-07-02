# Script que tenha apenas 2 registros, contendo cada um deles como chave o tipo de feijão e como valor a quantidade de feijão consumida

registro = {
    'feijoada': 0.00, 'feijao_verde': 0.00
}
valor_f = 0
valor_fv = 0
while True:
    print("-"*50)
    print(f'{"***** Cosumo de feijão na cantina *****":^50}')
    print("-"*50)
    print("Foram consumidos até o momento aproximadamente: ")
    for f,v in registro.items():
        print(f"- {v} quilos de {f}")
    print("-"*50)
    print(" [1] para registrar a venda de Feijoada")
    print(" [2] para registrar a venda de Feijão Verde")
    print("-"*50)
    num = int(input("- Digite: "))
    if num == 1:
        valor_f += float(input("Quantidade de Feijoada consumida em quilos: "))
        registro.update({'feijoada':valor_f})
    elif num == 2:
        valor_fv += float(input("Quantidade de Feijão verde consumido em quilos: "))
        registro.update({'feijao_verde':valor_fv})

    else: 
        break