from tkinter import *
import requests, json
import sqlite3

class App:
    def __init__(self):
        self.tela()
        self.widgets()
        self.janela.mainloop()


    def tela(self):
        self.janela = Tk()
        self.janela.title('Python + TKInter + BD (Sqlite)')
        self.janela.geometry('650x370')
        self.janela.eval('tk::PlaceWindow . center')
        self.janela.resizable(width = False, height = False)
        self.op = ''

    def widgets(self):

        self.Label_title = Label(background = 'Black', borderwidth = 2, font = 'Arial 20 bold', foreground = 'White', text = 'Controle de Alunos da Escola Internacional')
        self.Label_title.place(x = 0, y = 5, height = 50, width = 650)

        self.Label_aluno = Label(background = 'grey', font = 'Arial 12 bold', foreground = 'white', text = 'Aluno')
        self.Label_aluno.place(x = 500, y = 60, height = 30, width = 140)

        self.Button1 = Button(command=self.inserir, background = 'green', font = 'Arial 12 bold', foreground = 'white', text = 'Inserir')
        self.Button1.place(x = 510, y = 100, height = 30, width = 120)
        
        self.Button2 = Button(command=self.excluir, background = 'red', font = 'Arial 12 bold', text = 'Excluir', foreground = 'White')
        self.Button2.place(x = 510, y = 140, height = 30, width = 120)
        
        self.Button3 = Button(command=self.list_aprovados,background = 'orange', font = 'Arial 12 bold', text = 'Aprovados', foreground = 'White')
        self.Button3.place(x = 510, y = 180, height = 30, width = 120)
        
        self.Label_notas = Label(background = 'grey', font = 'Arial 12 bold', foreground = 'white', text = 'Notas')
        self.Label_notas.place(x = 500, y = 220, height = 30, width = 140)

        self.Button4 = Button(command=self.adi_notas, background = 'green', font = 'Arial 12 bold', foreground = 'white', text = 'Adi / alt')
        self.Button4.place(x = 510, y = 260, height = 30, width = 120)
        
        self.Button5 = Button(command=self.ok ,background='lightblue', font = 'Arial 12 bold', text = 'OK')
        self.Button5.place(x = 500, y = 320, height = 40, width = 140)

        self.Label1 = Label(font = 'Arial 16 bold', text = 'Nome:')
        self.Label1.place(x = 15, y = 70, height = 30, width = 70)
        
        self.Entry1 = Entry(borderwidth = 3, font = 'Arial 16 bold', foreground = 'blue', justify = 'left')
        self.Entry1.place(x = 105, y = 60, height = 45, width = 370)

        self.Label2 = Label(font = 'Arial 14 bold', text = 'Nota 1:')
        self.Label2.place(x = 25, y = 130, height = 30, width = 70)
        
        self.Entry2 = Entry(borderwidth = 3, font = 'Arial 14 bold', foreground = 'blue', justify = 'left')
        self.Entry2.place(x = 105, y = 120, height = 45, width = 100)     

        self.Label3 = Label(font = 'Arial 14 bold', text = 'Nota 2:')
        self.Label3.place(x = 25, y = 200, height = 30, width = 70)
        
        self.Entry3 = Entry(borderwidth = 3, font = 'Arial 14 bold', foreground = 'blue', justify = 'left')
        self.Entry3.place(x = 105, y = 190, height = 45, width = 100)     

        self.Label4 = Label(font = 'Arial 14 bold', text = 'Nota 3:')
        self.Label4.place(x = 220, y = 130, height = 30, width = 70)
        
        self.Entry4 = Entry(borderwidth = 3, font = 'Arial 14 bold', foreground = 'blue', justify = 'left')
        self.Entry4.place(x = 305, y = 120, height = 45, width = 100)     

        self.Label5 = Label(font = 'Arial 14 bold', text = 'Nota 4:')
        self.Label5.place(x = 220, y = 200, height = 30, width = 70)
        
        self.Entry5 = Entry(borderwidth = 3, font = 'Arial 14 bold', foreground = 'blue', justify = 'left')
        self.Entry5.place(x = 305, y = 190, height = 45, width = 100)     

        self.LabelFrame = LabelFrame(text = 'Lista de alunos aprovados')
        self.LabelFrame.place(x = 25, y = 250, height = 70, width = 420,anchor = 'nw')

        self.Label_frame = Label(font = 'Arial 16 bold', text = '')
        self.Label_frame.place(x = 30, y = 270, height = 30, width = 390, anchor = 'nw')

        self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Começe a inserir alunos!', background='grey')
        self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')


    def inserir(self):
        self.op = 'inserir'
        self.Entry1.delete(0,END)
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)

        
    def excluir(self):
        self.op = 'excluir'
        self.Entry1.delete(0,END)
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)

        self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Insira o nome do aluno para excluir', background='grey')
        self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')


    def list_aprovados(self):
        self.op = 'list_aprovados'
        self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Confirme com OK', background='grey')
        self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')
        
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)

    def adi_notas(self):
        self.op = 'notas'
        self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Adicione as notas do aluno', background='grey')
        self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')
        
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        self.Entry5.delete(0,END)

    def ok(self):

        if self.op == 'inserir':
            conexao = sqlite3.connect('escolainternacional.db') 
            sql = conexao.cursor()
            sql.execute(f"INSERT INTO alunos (nome) VALUES ('{self.Entry1.get()}')")
            conexao.commit()
            conexao.close()
            self.op = ''
            self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Aluno inserido com sucesso', background='grey')
            self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')

        elif self.op == 'excluir':
            conexao = sqlite3.connect('escolainternacional.db') 
            sql = conexao.cursor()
            sql.execute(f"DELETE FROM alunos WHERE nome == '{self.Entry1.get()}'")
            conexao.commit()
            conexao.close()
            self.op = ''
            self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'ALuno excluido com sucesso', background='grey')
            self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')


        elif self.op == 'list_aprovados':
            self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Alunos aprovados', background='grey')
            self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')
        
            lista_media = []
            alunos_aprovados = ''

            conexao = sqlite3.connect('escolainternacional.db') 
            sql = conexao.cursor()
            sql.execute("SELECT * FROM alunos")
            nome_alunos = sql.fetchall()
            print(nome_alunos)

            for t in nome_alunos:
                print(t[0])
                soma = int(t[1]) + int(t[2])  + int(t[3])  + int(t[4]) 
                media = soma/4
                lista_media.append(media)

            for n ,i in enumerate(lista_media):
                if i >= 60:
                    alunos_aprovados += f' {nome_alunos[n][0]}'
            
            self.Label_frame = Label(font = 'Arial 16 bold', text = f'{alunos_aprovados}')
            self.Label_frame.place(x = 30, y = 270, height = 40, width = 420, anchor = 'nw')
            
            conexao.commit()
            conexao.close()
            self.op = ''


        elif self.op == 'notas':
            self.Label_info= Label(fg='white', font = 'Arial 12 bold', text = 'Notas adicionadas', background='grey')
            self.Label_info.place(x = 25, y = 330, height = 30, width = 420, anchor = 'nw')
        
            conexao = sqlite3.connect('escolainternacional.db') 
            sql = conexao.cursor()
        
            sql.execute(f"UPDATE alunos SET nome = '{self.Entry1.get()}' WHERE nome = '{self.Entry1.get().capitalize()}'")
            sql.execute(f"UPDATE alunos SET nota1 = '{self.Entry2.get()}' WHERE nome = '{self.Entry1.get()}'")
            sql.execute(f"UPDATE alunos SET nota2 = '{self.Entry3.get()}' WHERE nome = '{self.Entry1.get()}'")
            sql.execute(f"UPDATE alunos SET nota3 = '{self.Entry4.get()}' WHERE nome = '{self.Entry1.get()}'")
            sql.execute(f"UPDATE alunos SET nota4 = '{self.Entry5.get()}' WHERE nome = '{self.Entry1.get()}'")

            conexao.commit()
            conexao.close()
            self.op = ''

import os

os.remove('escolainternacional.db')
conexao = sqlite3.connect('escolainternacional.db') 
sql = conexao.cursor()
sql.execute('CREATE TABLE alunos (nome, nota1, nota2, nota3, nota4)')
conexao.commit()
conexao.close()

aplicacao = App()




