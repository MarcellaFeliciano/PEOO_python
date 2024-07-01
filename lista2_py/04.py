#script que solicita o preço de três produtos e informe qual produto você deve comprar
print("-="*20)
produto_1 = float(input("- Valor do 1° produto: "))
produto_2 = float(input("- Valor do 2° produto: "))
produto_3 = float(input("- Valor do 3° produto: "))
if produto_1<produto_2 and produto_1<produto_3:
    print(f"Você deve comprar o produto 1 pois custa R${produto_1}")
elif produto_2<produto_1 and produto_2<produto_3:
    print(f"Você deve comprar o produto 2 pois custa R${produto_2}")
elif produto_3<produto_1 and produto_3<produto_1:
    print(f"Você deve comprar o produto 3 pois custa R${produto_3}")
print("-="*20)