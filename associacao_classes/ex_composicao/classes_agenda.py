class Amigo:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def inserir_telefone(self,ddd,numero):
        self.telefones.append(Telefone(ddd,numero)) 
        #pega da classe Telefone os atributos ddd e numero

    def listar_telefones(self):
        for telefone in self.telefones:
            print(telefone.ddd, telefone.numero)

class Telefone:
    def __init__(self,ddd,numero):
        self.ddd = ddd
        self.numero = numero