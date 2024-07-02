from classes_biblioteca import *
import os

estante_romance = Estante('romance')
estante_suspense = Estante('suspense')
estante_desenho = Estante('desenho')
estante_fantasia = Estante('fantasia')

print("-="*30)
num_livros = int(input("- Quantos livros você quer adicionar a biblioteca? "))

for i in range(num_livros):
    os.system('cls')
    livro = None
    print("-="*20)
    print(f"        Informações do {i+1}° livro")
    titulo = input(" Nome do livro: ")
    genero = input(" Gênero: ")
    num_paginas = input(" Número de páginas: ")
    
    livro = Livro(titulo=titulo, genero=genero, num_paginas=num_paginas)
    

    if genero == 'romance':
        estante_romance.livros.append(livro)

    elif genero == 'suspense':
        estante_suspense.livros.append(livro)

    elif genero == 'desenho':
        estante_desenho.livros.append(livro)

    elif genero == 'fantasia':
        estante_fantasia.livros.append(livro)

    else:
        print('Estante desse genero literário não encontrado!')
    

quant_romance = len(estante_romance.livros)
quant_suspense = len(estante_suspense.livros)
quant_fantasia = len(estante_fantasia.livros)
quant_desenho = len(estante_desenho.livros)

os.system('cls')

print("-"*40)
print(f'{"Estantes da biblioteca":^40}')
print("-"*40)
if quant_romance != 0:
    print(f"{'R O M A N C E':^40}")
    print("-"*40)
    for n,liv in enumerate(estante_romance.livros):
        print(f' {n+1}° Livro - Título: {liv.titulo}')

if quant_suspense != 0:
    print("-"*40)
    print(f"{'S U S P E N S E':^40}")
    print("-"*40)
    for n,liv in enumerate(estante_suspense.livros):
        print(f' {n+1}° Livro - Título: {liv.titulo}')

if quant_fantasia != 0:
    print("-"*40)
    print(f"{'F A N T A S I A':^40}")
    print("-"*40)
    for n,liv in enumerate(estante_fantasia.livros):
        print(f' {n+1}° Livro - Título: {liv.titulo}')

if quant_desenho != 0:
    print("-"*40)
    print(f"{'D E S E N H O':^40}")
    print("-"*40)
    for n,liv in enumerate(estante_desenho.livros):
        print(f'{n+1}° Livro - Título: {liv.titulo}')

print("-"*40)
print()

        







