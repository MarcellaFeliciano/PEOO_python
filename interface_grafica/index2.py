from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames_da_tela()
        self.widgets()
        self.janela.mainloop()

    def tela(self):
        self.janela.title("Aplicativo Internacional")
        self.janela.geometry('800x700')

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela)
        self.frame_1['height'] = 700
        self.frame_1['width'] = 800
        self.frame_1['bd'] = 3
        self.frame_1['bg'] = '#FFC0CB'
        self.frame_1.pack()

    def widgets(self):
        self.texto_1 = Label(self.frame_1,
        text='Roberto Carlos',
        bg='black',
        fg='white',
        font= ('Arial','20','bold'))
        self.texto_1.pack()

        self.botao_1 = Button(self.frame_1, command=self.mudar,
        text='Clique aqui!',
        font=('Verdana','20','bold'),
        bg = 'purple',
        fg = 'yellow'
        )
        self.botao_1.pack(side='top')

        self.botao_2 = Button(self.frame_1, command=self.descer,
        text='Clique!',
        font=('Verdana','20','bold'),
        bg = 'purple',
        fg = 'yellow',
        width=600
        )
        self.botao_2.pack(side='bottom')

    def mudar(self):
        if self.texto_1['text'] == 'Roberto Carlos':
            self.texto_1['text'] = 'Ricardo Kleber'
        else:
            self.texto_1['text'] = 'Roberto Carlos'
        
    def descer(self):
        self.botao_1.pack(side='bottom')

aplicacao = App() # aplicação é uma instancia da classe biblioteca