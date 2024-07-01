#script de calculo de aumento salarial
print("-"*45)
print(f'{"Calculador de salario com aumento de 9%":^45}')
print("-"*45)
salario = float(input("- Salario atual: "))
aumento = 9/100 * salario
novo_salario = salario + aumento
print(f"O salario com o aumento de 9% é R${novo_salario}")
print("-"*45)