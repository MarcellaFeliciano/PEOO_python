"""x = int(input('Digite um Número: '))
y = int(input('Digite outro Número: '))
if y == 0:
   raise ValueError('y não pode ser zero')
print(x/y)

------------------------------"""

def somapositivos(a,b):
   if a < 0 or b < 0:
         raise ValueError('Valor Negativo Informado')
   return a+b

   print(somapositivos(4,-3))

