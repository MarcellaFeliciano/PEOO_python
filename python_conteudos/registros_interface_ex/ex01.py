from tkinter import *

import pickle

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('400x400')
        self.janela.title('Editorde texto')


        self.botao1  = Button(self.janela,text='oi', command= self.add_text)
        self.botao1.pack()
        self.caixa_texto = Text(self.janela, height=20,bg='yellow')
        self.caixa_texto.pack()


        self.janela.mainloop()

    def add_text(self):
        arq = open('texto_nao-binario.txt','r')
        conteudo= arq.read()
        self.caixa_texto.delete(0.0,END)
        self.caixa_texto.insert('0.0', conteudo)


rodar = App()
