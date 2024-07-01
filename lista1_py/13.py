#script que mostra compra com desconto no pix
print("-"*40)
compra = float(input(" Digite o valor da compra: "))
desconto = (3/100) * compra
valor = desconto + compra
print("-"*40)
print(f'{"- Compra no PIX -":^40}')
print("-"*40)
print(f"  Valor da compra - R${compra}")
print(f"  Desconto de 3% - R${desconto}")
print(f"  Valor final - R${valor}")
print("-"*40)