#script que solicita ao usuário a digitação do seu primeiro nome, separe as letras e armazene no formato de lista e, em seguida,
# faça o mesmo com o sobrenome (solicite a digitação e armazene em outra lista). Exiba então: o número de letras do nome,
# o número de letras do sobrenome e ao final informe: Seu nome completo é (e exiba o nome completo a partir da concatenação das duas listas).

lista_nome = []
lista_sobrenome = []
l_nome = 0
l_sobrenome = 0
nome = input(f"- Digite o seu nome: ")
sobrenome = input(f"- Digite o seu sobrenome: ")
for l in nome:
    l_nome += 1
    lista_nome.append(l)
for l in sobrenome:
    l_sobrenome += 1
    lista_sobrenome.append(l)
nome_completo = nome +" "+ sobrenome
print("-="*35)
print(f"O nome tem {l_nome} letras!")
print(f"O sobrenome tem {l_sobrenome} letras!")
print(f"Nome completo: {nome_completo} ")
print("-="*35)


