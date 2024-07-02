class ContaCorrente:
    def __init__(self,nome):
        self.cliente_nome = nome
        self.saldo = 0


    def verSaldo(self):
        return self.saldo

    def depositar(self,valor):
        valor_inicial = self.saldo
        valor_depositar = valor + valor_inicial
        self.saldo = valor_depositar

    def sacar(self,valor):
        saldo = self.saldo
        try:
            if saldo >= valor:
                saldo -= valor
                self.saldo = saldo
            else:
                raise Exception("O valor que você deseja sacar é superior ao saldo!")
        except Exception as erro:
            print("="*50)
            print("Erro ao sacar!")
            print(f"{erro}")
            print(f"Só é possível fazer saques de até {ContaCorrente.verSaldo(self)}$")
            print("="*50)



print("Bem vindo ao Banco")
nome = input("Informa o seu nome: ")
cliente = ContaCorrente(nome)
print("Assessando sua conta corrente..")
while True:
        print('''
        =======================================
        Banco - Conta Corrente
        =======================================
        [1] Consultar Saldo
        [2] Depositar
        [3] Sacar
        [0] Sair
        =======================================
        ''')
        opcao = int(input('Informe a Opção: '))

        if opcao == 1:
            print(f'Cliente: Nome: {cliente.cliente_nome} | Saldo: {cliente.verSaldo()}')
            
        elif opcao == 2:
            valor = float(input(f'Valor a Depositar para a conta de {nome} : '))
            cliente.depositar(valor)        
            print(f'Cliente: Nome: {nome} | Saldo: {cliente.verSaldo()}')

        elif opcao == 3:
            valor = float(input(f'Valor a Sacar da conta de {nome} : '))
            cliente.sacar(valor)        
            print(f'Cliente: Nome: {nome} | Saldo: {cliente.verSaldo()}')
        
        
        elif opcao == 0:
            print("Saindo do Banco!")
            break
