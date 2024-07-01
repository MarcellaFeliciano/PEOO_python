import math
print("-"*50)
def num_negativo(n):
    if n < 0:
        raise Exception('Número negativo! Digite um número positivo!')

while True:
    num = float(input('Digite um número para saber a raiz quadrada: '))
    try:
        num_negativo(num)

    except Exception as erro:
        print(f"{erro}") 
    else:
        print(f"A raiz de {num} é {math.sqrt(num)}")
        break
print("-"*50)