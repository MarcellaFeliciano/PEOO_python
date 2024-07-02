import random

class Conta:
    def __init__(self,nome):
        self.cliente_nome = nome
        self.num_conta = None
        self.__saldo = 0

    def get_saldo(self):
        return int(self.__saldo)

    def set_saldo(self,valor):
        self.__saldo = valor


    def consultar_saldo(self):
        saldo = self.get_saldo()
        return saldo

    def depositar(self,valor):
        valor_inicial = Conta.get_saldo(self)
        valor_depositar = valor + valor_inicial
        Conta.set_saldo(self,valor_depositar)


    def sacar(self,valor):
        saldo = Conta.get_saldo(self)
        if saldo >= valor:
            saldo -= valor
            Conta.set_saldo(self,saldo)

    def gera_conta(self):
        x = str(random.randint(0,9))
        for i in range(5):
            x = x + str(random.randint(0,9))
        return x



class Conta_corrente(Conta):
    def __init__(self, nome):
        super().__init__(nome)
        self.__limite = 1000


    def get_limite(self):
        return int(self.__limite)

    def set_limite(self,valor):
        self.__limite = valor


    def alterar_limite(self, valor):
        self.set_limite(valor)

    


class Conta_poupanca(Conta):
    def __init__(self):
        super().__init__()
        self.__taxa_de_juros = 0


    def set_taxa_de_juros(self, valor):
        self.__taxa_de_juros = valor


    def aplicar_juros(self, taxa):
        self.__saldo += self.__saldo*self.__taxa_de_juros

