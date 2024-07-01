# o while serve par acontinuar em um lopp ate não cair em nenhuma das exceções definidas dentro do while,
#  ou seja se o codigo não apresentar nenhum erro ele sai do while com o break  


while True:
   try:
       x = int(input('Digite um Número: '))
       y = int(input('Digite outro Número: '))
       print(f'{x}/{y} = {x/y}') 
       # o print do calculo é necessaro para saber se vai dar erro ou surgir um erro! nem que seja necessario 
       # ter varios trys para fazer o codigo ir avançando!
   except ValueError:
       print('Eu disse um número!!!')
   except ZeroDivisionError:
       print('Divisão por Zero Não Pode!!!')
   else:
       break
