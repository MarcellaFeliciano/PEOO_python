#script que solicita ao usuário e armazena em uma lista quatro notas e ao final apresenta: a média aritmética, a maior nota e a menor nota.
lista = []
soma = 0
cont = 0
maior = 0
menor = 0 
print("-="*20)
print(f'{"Atribua o valor das 4 notas":^40}')
print("-"*40)
for i in range(1,5):
    nota = float(input(f"- Digite a {i}° nota: "))
    lista.append(nota)
for pos, n in enumerate(lista):
    soma += n
    cont += 1
    if pos == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print("-"*40)
print(f"A média das notas é {media:.1f}")
print(f"A maior nota é {maior} e a menor nota é {menor}")
print("-="*20)
