#script que calcula a hipotenusa
print("-="*25)
print("   Informe os valores do triangulo retangulo")
print("-"*50)
cateto_adjacente = float(input("- Cateto adjacente: "))
cateto_oposto = float(input("- Cateto oposto: "))
calculo = (cateto_adjacente**2) + (cateto_oposto**2)
hipotenusa = calculo ** (1/2)
print(f" O valor da hipotenusa é igual a {hipotenusa}")
print("-="*25)