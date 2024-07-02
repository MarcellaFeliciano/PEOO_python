from classes_registro import *
import os

biblioteca = []
while True:
    os.system('cls')
    historico = Historico()
    print("-"*40)
    print("Adicionar histórico de um livro")
    print("-"*40)
    nome = input(" Título do livro: ")
    if nome.lower() == 'sair':
        print("Saindo do registro..")
        break

    data = input("- Data do emprestimo: ")
    historico.emprestimos.append(data)

    while True:
        resp = input(" Quer adicionar mais um histórico? [S/N] ").upper()
        if resp == 'S':
            data = input("- Data do emprestimo: ")
            historico.emprestimos.append(data)
        else:
            break

    livro = Livro(titulo=nome)
    livro.adicionar_emprestimo(historico)
    biblioteca.append(livro)

for n,liv in enumerate(biblioteca):
    print("-"*30)
    print(f"         {n+1}° Livro")
    print("-"*30)
    print(f" Título - {liv.titulo}")
    print(f'{"Registro dos emprestimos":^30}')

    for n,d in enumerate(liv.emprestimo.emprestimos):
        print(f"  Data - {d}")



