#script que recebe o valor de um ‘depósito inicial’ em uma poupança e a ‘taxa de juros mensal'
print('-='*20)
print(f'{"Calculador de juros":^40}')
print('-='*20)
depos_inicial = float(input("- Valor do deposito inicial: "))
taxa = int(input("- Taxa de juros: (%) "))
cont = 0
valor = depos_inicial
juros_total = 0
juro = 0
while cont != 12:
    cont+=1
    juro = (taxa/100)* valor
    valor = valor - juro
    juros_total += juro
    print("-"*40)
    print(f" Saldo do {cont}° mês: R$ {valor:.2f}")
print("-"*40)
print(f" O valor total de juros foi de R${juros_total:.2f}")
print('-='*20)

 