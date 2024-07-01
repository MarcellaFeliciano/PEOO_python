""" 
-----------------------------------------------
    Associação / instanciação

- atributos/metodos de uma classe que vão comversaar com os atrinutos/metodos de outra classe

- classes -
class Emprego:
    def __init__(self):
    self.cargo = 'em treinamento'
    self.salario = 1320.0

class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.emprego = None

- arquivo -
from classes import Emprego, Pessoa

funcionario = Pessoa('Jorgin')
funcionario.emprego = Emprego() -- está instaciando o atributo (emprego) á classe (emprego)

#o atributo de uma classe (objeto) recebe os atributos de outra classe

print(funcionario.nome)
print(funcionario.emprego.cargo)
print(funcionario.emprego.salario)

----------------------------
aluno = Aluno('chico')
aluno.boletim = Boletim()
---------------------------



-----------------------------
- agregação 

agregar classes/objetos independentes, que se juntam, mais cada um trabalha sozinho independente do outros


- composição

onde um ou os dois só funcionam um com o outro, não são independentes (a composição precisa um do outro)





"""
