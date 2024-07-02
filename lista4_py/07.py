#script que imprima na tela os números de 1 a 20, um abaixo do outro e, em seguida, no formato de lista (um ao lado do outro, entre colchetes, separados por vírgula).

lista = []
print("-="*35)
print(f'{"C O N T A G E M  DE 1 Á 20":^70}')
print("-"*70)
for i in range(1,21):
    print(i)
    lista.append(i)
print("-"*70)
print(lista)
print("-="*35)

