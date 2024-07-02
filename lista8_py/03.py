# Programa que utilize funções da biblioteca ‘random’ para criar sugestões de senhas aleatórias.

from random import randint

def main():
    arq_senhas = open('senha.txt','wt+')
    print("-"*35)
    print(f'{"Criador de senhas":^35}')
    print("-"*35)
    quant = int(input("- Digite a quantidade de senhas:"))
    for q in range(0,quant):
        senha = ''
        num = int(input(f'Qual o tamanho da {q+1}° senha? '))
        for i in range(0,num):
            n = randint(0,9)
            senha += str(n)
        arq_senhas.write(f'Senha[{q+1}]-{senha}\n')
    arq_senhas.close()
    print("-"*35)

if __name__ == '__main__': # chamada da funcao principal
    main()



