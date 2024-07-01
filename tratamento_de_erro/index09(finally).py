try:
   x = int(input('Digite um Número: '))
   y = int(input('Digite outro Número: '))
except ValueError:
   print('Valor Inválido!!!')
else:
   try:
       print(f'{x}/{y} = {x/y}')
   except ZeroDivisionError:
       print('Valor Inválido!!! divisão por zero!')
finally:
   print('Terminei meu serviço. Obrigado!')
