try:
   x = int(input('Digite um Número: '))
   y = int(input('Digite outro Número: '))
   print(x/y)
except (ValueError, ZeroDivisionError):
   print('Tem que ser número e não ser dividido por zero!!!')
except:
   print('Erro Desconhecido!!!')
