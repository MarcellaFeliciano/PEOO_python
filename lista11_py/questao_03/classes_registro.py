
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestimo = None


    def adicionar_emprestimo(self, historico):
        self.emprestimo = historico
    
    
class Historico:
    def __init__(self):
        self.emprestimos = []




