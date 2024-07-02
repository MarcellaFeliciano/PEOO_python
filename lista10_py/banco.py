

from lib_banco import Conta
import os

def main():

    cliente = False

    while True:
        print('''
        =======================================
        Banco Internacional
        =======================================
        [1] Cadastrar Cliente
        [2] Gerar Número da Conta
        [3] Consultar Saldo
        [4] Depositar
        [5] Sacar
        [0] Sair
        =======================================
        ''')

        opcao = int(input('Informe a Opção: '))

        if opcao == 1:
            
            nome = input('Digite o Nome do Cliente para Cadastrar: ')
            cliente = Conta(nome)
            
            print(f'Cliente Cadastrado: {cliente.cliente_nome}')

        elif opcao == 2:
            
            if cliente != False:
                cliente.num_conta = cliente.gera_conta()
                print(f'Cliente: Nome: {cliente.cliente_nome} | Número da Conta: {cliente.num_conta}')

        elif opcao == 3:
            
            if cliente != False:
                print(f'Cliente: Nome: {cliente.cliente_nome} | Número da Conta: {cliente.num_conta} | Saldo: {cliente.get_saldo()}')

        elif opcao == 4:
            
            if cliente != False:
                valor = float(input(f'Valor a Depositar para {cliente.cliente_nome} : '))
                cliente.depositar(valor)        
                print(f'Cliente: Nome: {cliente.cliente_nome} | Número da Conta: {cliente.num_conta} | Saldo: {cliente.get_saldo()}')

        elif opcao == 5:
        
            if cliente != False:
                valor = float(input(f'Valor a Sacar da conta de {cliente.cliente_nome} : '))
                cliente.sacar(valor)        
                print(f'Cliente: Nome: {cliente.cliente_nome} | Número da Conta: {cliente.num_conta} | Saldo: {cliente.get_saldo()}')
        
        elif opcao == 0:
            break

if __name__ == '__main__':
    main()