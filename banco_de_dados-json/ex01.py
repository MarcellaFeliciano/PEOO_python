# No banco de dados SQLite há tabelas onde há os registros

# https://sqliteviewer.app  ver os qrquivos de banco de dados

import sqlite3

# SELECT * FROM Customers; - seleciona todas as tabelas



conexao = sqlite3.connect('banco.db') 
# acessa/conecta ou cria se não existir um banco SQLite
# cria um arquivo db com o nome 'banco.db'

sql = conexao.cursor()
# o metodo cursor associado a 'SQL' cria a a instacia associada a conexão - 


# sql.execute('CREATE TABLE test (nome, telefone)')

# sql.execute('instrução SQL') 
# o texto  - instrução sql - cri a tabela
# creat table e o nome da tabela cria a tabela

sql.execute('CREATE TABLE alunos (matricula, nome, curso)')
# se já existir o arquivo d ebanco de dados não prcisa do creat table

sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('123','Marela','Vestuario')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('456','Vevelyng','Eletro')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('789','Kekeu','InfoWeb')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('101','Prefeito George','InfoWeb')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('111','Popó','Alimentação')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('173','Costela','Textil')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('135','Italo Green','Natação')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('123','Xuão','Hospício')")
sql.execute("INSERT INTO alunos (matricula, nome, curso) VALUES ('123','Hiandro','Fuleragem')")

# sql.execute("INSERT INTO teste (nome,telefone) VALUES ('RK','9999-9999')")
# adiciona valores as tabelas


# CRUD - CRIAT / READ / UPDATE / Delete


conexao.commit() # metodo que diz os dados que forem inseridos podem ser inseridos no banco e não apenas na memoria
conexao.close() 

sql.execute("SELECT * FROM alunos")
my_alunos = sql.fetchall()
print(type(sql.execute))
# seleciona todos os elementos da tabela
# manipular registros selecionados (forma de lista) = sql.fetchall() 
# pega todos os 'valores - regiostros de uma tabela do banco ' e transforma em uma lista!



# --------------------------
#  import sqlite3


# conexao = sqlite3.connect('banco.db') 

# sql = conexao.cursor()

# sql.execute("SELECT * FROM alunos")
# my_alunos = sql.fetchall()
# print(type(sql.execute))
# print(my_alunos[0][1]) # mostra o elemento 0 da lista em uma tupla / o valor 1 da tupla