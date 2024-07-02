#script que inicia com um saldo de 1.000 e permite que o usuário informe valores de compras
print("-"*35)
print('Início das compras!')
print("Saldo inicial - R$ 1000.00")
saldo = 1000
cont = 0
while saldo != 0:
    print("-"*35)
    compra = float(input("- Digite o valor do produto: "))
    if saldo >= compra:
        print("-"*35)
        print("Compra efetuada com sucesso!")
        saldo = saldo - compra
        cont += 1
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print("-"*35)
        print("Não há saldo para esta compra")
        print(f"Saldo atual: R${saldo:.2f}")
print("-"*35)