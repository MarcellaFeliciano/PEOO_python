try:
  x = int(input('Digite um Número: '))
  y = int(input('Digite outro Número: '))
  print(x/y)

except KeyboardInterrupt as erro:
  print(f'Erro Encontrado = {erro} ')
  print(f'Tipo/Classe do Erro Encontrado = {type(erro)} ')

except Exception as erro: # se ocorrer uma exceção gurade essa exceção como um erro
  print(f'Erro Encontrado = {erro} ')
  print(f'Tipo/Classe do Erro Encontrado = {type(erro)} ')