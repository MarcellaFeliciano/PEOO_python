def somapositivos(a,b):
   assert a > 0, 'a não pode ser negativo'
   assert b > 0, 'b não pode ser negativo'
   return a+b

print(somapositivos(4,-3))
