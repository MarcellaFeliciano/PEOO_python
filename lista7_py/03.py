# Script que peça para o usuário registrar um estoque de produtos. Cada produto possui um código, um preço e uma quantidade.

registro = dict()
for i in range(1,6):
    print("-"*30)
    print(f"         {i}° Produto")
    print("-"*30)
    nome = input(" - Nome do produto: ")
    codigo = int(input(" Código do produto: "))
    preco = float(input(" Preço do produto: R$ "))
    quantidade = int(input(" Quantidade do produto: "))
    estoque = [codigo, preco, quantidade]
    registro[nome] = estoque

quant_total = 0
valor_total = 0

for n in registro.values():
    quant_total += n[2]
    valor_total += n[1]
print()
print("-"*40)
print(f'{"Relatório do Estoque":^40}')
print("-"*40)
print(f" Quantidade total de produtos: {quant_total}")
print(f" Valor total do estoque: {valor_total}")
print("-"*40)
