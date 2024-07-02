# programa que implementa uma agenda que guarda registros com os campos: CPF (inteiro), nome (string), telefone (string) em um arquivo chamado agenda.txt.
 
#importação de bibliotecas
from time import sleep
from colorama import Fore

# função principal - agenda
def main():
    n = 0
    if n == 0:
        cria_agenda()
        n = 1
    while True:
        menu = [0,1,2,3]
        print()
        print("-"*45)
        print(Fore.BLUE, f"{'A G E N D A':^45}", Fore.WHITE)
        print("-"*45)
        print(" [0] Sair da agenda")
        print(" [1] Adicionar um registro")
        print(" [2] Apagar um registro")
        print(" [3] Mostrar lista de registros")
        print("-"*45)
        print(Fore.YELLOW)
        resp = int(input("- Escolha uma opção: "))
        print(Fore.WHITE)

        while True:
            if resp not in menu:
                print(Fore.RED, "Opção não encontrada! Siga o menu da agenda!", Fore.WHITE)
                resp = int(input("Sua opção: "))
            else:
                break
        
        if resp == 0:
            print(Fore.RED)
            print("Saindo da agenda.", end='', flush=True)
            sleep(0.5)
            print(".", end='', flush=True)
            sleep(0.5)
            print(".")
            print(Fore.WHITE)
            break

        elif resp == 1:
            print("-"*45)
            print(f'{"-- Adicionar registro --":^45}')
            nome = input("- Nome: ")
            cpf = int(input("- CPF: "))
            telefone = input("- Telefone: ")
            adicionar(nome,cpf,telefone)

        elif resp == 2:
            print("-"*45)
            print(f'{"-- Apagar Registro --":^45}')
            nome = input("Nome: ")
            apagar(nome)

        elif resp == 3:
            sleep(0.5)
            print("~"*45)
            print(f'{"Listagem da agenda":^45}')
            mostrar()
        
# criar agenda
def cria_agenda():
    agenda = open('agenda_lista_08.txt','wt+')
    agenda.close()


# função de adicionar um registro
def adicionar(nome='desconhecido',cpf=0,telefone='0'):
    agenda = open('agenda_lista_08.txt','a')

    #testando comandos que vi em um video! :)
    try:
        agenda.write(f'{nome};{cpf};{telefone}\n')
    except:
        print("Houve um erro ao adicionar o registro!")
    else:
        print(Fore.GREEN, f" Registro de {nome.capitalize()} adicionado a agenda!", Fore.WHITE)
        agenda.close()


# função de apagar um registro
def apagar(nome):
    situacao = ''
    agenda = open('agenda_lista_08.txt','rt+')
    conteudo = agenda.readlines()
    agenda.close()

    for linha in conteudo:
        dados = linha.split(';')

        if dados[0] == nome:
            conteudo.remove(linha)
            situacao = 'concluido'
            print(Fore.RED, f' Registro de {nome.capitalize()} deletado!', Fore.WHITE)
    if situacao != 'concluido':
        print(Fore.RED, "Registro não encontrado!", Fore.WHITE)
        
    agenda = open('agenda_lista_08.txt','w')
    for l in conteudo:
        dados = l.split(';')
        agenda.write(f'{dados[0]};{dados[1]};{dados[2]}')
    agenda.close()


# função de mostrar a lista de registros
def mostrar():

    print("~"*45)
    print(" Nome      |     CPF     |    Telefone")
    print("-"*45)
    agenda = open('agenda_lista_08.txt','r')

    for linha in agenda:
       dados = linha.split(';')
       dados[2] = dados[2].replace('\n','')
       print(f'{dados[0].capitalize():<10}  {dados[1]:<15} {dados[2]:<10}')
    print("~"*45)
    sleep(3)
    agenda.close()


if __name__ == '__main__': # chamada da funcao principal
    main()