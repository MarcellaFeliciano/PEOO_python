#script que calcula valor do produto menos o desconto
print('-='*30)
compra = float(input("- Valor do produto: "))
desconto = int(input("- Valor percentual do desconto: "))
valor = (desconto/100) * compra
valor_final = compra - valor
print(f"O valor final do produto com desconto de {desconto}% é de R${valor_final}")
print('-='*30)