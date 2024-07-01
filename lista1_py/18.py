#script que calcula o IMC (indice de massa corporea)
print("-"*20)
print(f'{"Calculador de IMC":^20}')
print("-"*20)
peso = float(input("- Peso: "))
altura = float(input("- Altura: "))
imc = (altura**2) * peso
print(f"O IMC é igual a {imc:.2f}")
print("-"*20)
