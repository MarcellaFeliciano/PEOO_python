#script que recebe o nome, idade, estado civil e número de celular
print('-='*30)
print(f'{"Adicione as informações":^60}')
print('-='*30)

nome = input("- Nome:")
while len(nome)<=3:
    print("Erro encontrado!")
    nome = input('- Digite o nome novamente: ')
print("-"*60)

idade = int(input("- Idade: "))
while idade<10 or idade>100:
    print("Erro encontrado!")
    idade = int(input("- Digite a idade novamente: "))
print("-"*60)

print("Estados civis - Solteiro / Casado / Viuvo / Divorsiado")
while True:
    est_civil = input('- Estado civil: (S / C / V / D) ').upper()[0]
    if est_civil == 'S':
        est_civil = "Solteiro"
        break
    elif est_civil == 'C':
        est_civil = "Casado"
        break
    elif est_civil == 'V':
        est_civil = "Viuvo"
        break
    elif est_civil == 'D':
        est_civil = "Divorsiado"
        break
    print("Erro encontrado!")
print("-"*60)

numero = input("Número de telefone: ")
while len(numero)!=9:
    print("Erro encontrado!")
    numero = input("- Digite o número de telefone novamente: (9 digitos) ")

print("-="*30)
print(f'{"C A D A S T R O":^60}')
print("-="*30)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Estado civil: {est_civil}")
print(f"Numero de telefone: {numero}")
print("-="*30)