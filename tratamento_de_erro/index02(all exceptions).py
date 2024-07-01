try:
   x = int(input('Digite um Número: '))
   y = int(input('Digite outro Número: '))
   print(x/y)
except ValueError:
   print('Eu disse um número!!!')
except ZeroDivisionError:
   print('Divisão por Zero Não Pode!!!')
except:
   print('Erro Desconhecido!!!')
