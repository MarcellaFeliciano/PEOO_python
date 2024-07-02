#script que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Exemplo: 15/06/1974 = 15 de junho de 1974.
mes = [" de janeiro de "," de fevereiro de "," de março de "," de abril de "," de maio de "," de junho de "," de julho de "," de agosto de "," de setembro de "," de outubro de "," de novembro de "," de dezembro de ",]
num = ["01","02","03","04","05","06","07","08","09","10","11","12",]
print("-"*35)
print(f'{"- Data de nascimento - ":^35}')
print("-"*35)
data_nasc = input("Digite: (dd/mm/aaaa) ")
data = data_nasc.split("/")

for pos, n in enumerate(num):
    if n == data[1]:    
        data[1] = mes[pos]

print(f"Data: ", end='')
for i in range(0,len(data)):
    print(data[i], end='')
print()
print("-"*35)