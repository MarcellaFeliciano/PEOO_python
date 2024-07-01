"""
    HERANÇA
De forma similar, em POO as classes podem herdar
 - Atributos (propriedades)
 - Métodos (comportamento)


Permite a extensão de métodos e atributos previamente definidos na classe da qual está herdando suas características
 - Nova classe ➡ Subclasse (ou classe filha ou derivada)
 - Original ➡ Superclasse (ou classe pai ou ancestral ou base)

 class Subclasse(Superclasse):
    atributos (próprios)
	... 
	métodos (próprios)
    ...

Superclasse (características comuns)
Subclasses(características específicas)

 - Metodo construtor da subclasse da superclasse -

class Subclasse(Superclasse):
   def __init__(self):
       super().__init__()


Os métodos podem ser redefinidos em uma classe que herdou propriedades de outra!
~ Utilizar na subclasse o mesmo nome de um método da superclasse é chamado de sobrecarga (overload) ou sobrescrita (override)
---------------------------------------------------------------------------------------------------------------------------

  HERANÇA MULTIPLA

 - Capacidade de herdar características de mais de uma classe.
 A subclasse herda de duas (ou mais) superclasses todos os atributos e métodos!!!


class Subclasse(Superclasse1,Superclasse2, …):
atributos (próprios)
	... 
	métodos (próprios)
	...

---------------------------------------------------------------------------------------------------------------------------

   POLIMORFISMO

- Capacidade de um objeto poder ser referenciado de várias formas. - Sobrecarga (overload) ou sobrescrita (override)
- Capacidade de uma subclasse ter métodos com o mesmo nome dos métodos de sua superclasse

ex:
class Animal:
   quemsou = 'Sou um Animal'
   def som(self):
       return "Som genérico"

class Gato(Animal):
   def som(self):
       return "Miau"


"""
