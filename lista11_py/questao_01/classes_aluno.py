
class Aluno:
    def __init__(self, matricula, nome, turma, boletim):
        self.matricula = matricula
        self.nome = nome
        self.turma = turma
        self.boletim = boletim


class Notas:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (self.nota1 + self.nota2) /2
