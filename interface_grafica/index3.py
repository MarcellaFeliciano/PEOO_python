from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames_da_tela()
        self.widgets()
        self.janela.mainloop()
    
    def tela(self):
        self.janela.title("Janela Internacional")
        self.janela.geometry('300x200')
        self.janela.minsize(height=100, width=200)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela)
        self.frame_1.pack()

        self.frame_2 = Frame(self.janela)
        self.frame_2.pack()

        self.frame_3 = Frame(self.janela)
        self.frame_3.pack()

        self.frame_4 = Frame(self.janela)
        self.frame_4.pack()

    def widgets(self):
        self.texto_1 = Label(self.frame_1, text='Nome')
        self.texto_1.pack(side='left', pady=15)
        
        self.caixa1 = Entry(self.frame_1)
        self.caixa1.pack(side='left', pady=15)

        self.texto_2 = Label(self.frame_2, text='Telefone')
        self.texto_2.pack(side='left', pady=10)

        self.caixa2 = Entry(self.frame_2)
        self.caixa2.pack(side='left', pady=10)

        self.botao_inserir = Button(self.frame_3, text='Inserir', command=self.inserir)
        self.botao_inserir.pack(pady=10)

        self.texto_3 = Label(self.frame_4, text='Marcella123', bg='black', fg='yellow')
        self.texto_3.pack(pady=10)

    def inserir(self):
        self.texto_3['text'] = self.caixa1.get()+self.caixa2.get()
                
                
aplicacao = App() # aplicação é uma instancia da classe biblioteca