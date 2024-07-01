import warnings

def somapositivos(a,b):
   if a < 0 or b < 0:
       raise NameError('Valor Negativo Informado')
     #  warnings.warn('Valor Negativo Informado')
   return a+b

while True:
  try:
    print("-"*35)
    valor1 = int(input('- Insira um valor positivo:'))
    valor2 = int(input('- Insira outro valor positivo:'))
    print(f"A soma dos valores positivos é: {somapositivos(valor1, valor2)}")
    print("-"*35)

  except NameError as error1:    # tratamento do erro NameError
    print(f'-> Ocorreu um erro do tipo: {error1}!')
    print(" Inicie a operação novamete!")

  except ValueError as error2:
    print(f'-> Ocorreu um erro do tipo: {error2}!')
    print(" Inicie a operação novamete!")

  else:
    break





