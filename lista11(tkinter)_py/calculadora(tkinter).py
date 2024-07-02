from tkinter import *

class Calculadora:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames_tela()
        self.widgets()
        self.janela.mainloop()



    def tela(self):
        self.janela.title('Calculadora')
        self.janela.geometry('300x250')
        self.janela.configure(background='lightgrey')
        

    def frames_tela(self):
        self.frame0 = Frame(self.janela, background='lightgrey')
        self.frame0.pack(pady=20)

        self.frame1 = Frame(self.janela, background='lightgrey')
        self.frame1.pack()

        self.frame2 = Frame(self.janela, background='lightgrey')
        self.frame2.pack()

        self.frame3 = Frame(self.janela, background='lightgrey')
        self.frame3.pack()

        self.frame4 = Frame(self.janela, background='lightgrey')
        self.frame4.pack()

        self.frame5 = Frame(self.janela, background='lightgrey')
        self.frame5.pack()

    def widgets(self):
        self.texto_1 = Label(self.frame1, text='Valor 1 :', background='lightgrey')
        self.texto_1.pack(side='left', pady=1)

        self.texto_2 = Label(self.frame2, text='Valor 2 :', background='lightgrey')
        self.texto_2.pack(side='left', pady=1)

        self.caixa_1 = Entry(self.frame1)
        self.caixa_1.pack(side='left', padx=10, pady=1)

        self.caixa_2 = Entry(self.frame2)
        self.caixa_2.pack(side='left', padx=10, pady=1)

        self.bt_somar = Button(self.frame3, text='+', width=4, background='lightgrey', command=self.somar)
        self.bt_somar.pack(side='left', pady=10)

        self.bt_subtrair = Button(self.frame3, text='-', width=4, background='lightgrey', command=self.subtrair)
        self.bt_subtrair.pack(side='left', pady=10, padx=2)

        self.bt_multiplicar = Button(self.frame3, text='*', width=4, background='lightgrey', command=self.multiplicar)
        self.bt_multiplicar.pack(side='left', pady=10, padx=2)

        self.bt_dividir = Button(self.frame3, text='/', width=4, background='lightgrey', command=self.dividir)
        self.bt_dividir.pack(side='left', pady=10, padx=2)

        self.mostrar_resutado = Label(self.frame4, text='=', background='lightgrey')
        self.mostrar_resutado.pack(side='left', pady=5, padx=0)

        self.resutado = Label(self.frame4, text='', width=15, background='lightgrey')
        self.resutado.pack(side='left', pady=5)

        self.bt_limpar = Button(self.frame5, text='Limpar', width=10, background='lightgrey', command=self.limpar)
        self.bt_limpar.pack(side='left', pady=10, padx=3)

        self.bt_sair = Button(self.frame5, text='Sair', width=7, background='lightgrey', command=self.sair)
        self.bt_sair.pack(side='left', pady=10)


    def somar(self):
        n1 = int(self.caixa_1.get())
        n2 = int(self.caixa_2.get())
        self.resutado['text'] = n1 + n2


    def subtrair(self):
        n1 = int(self.caixa_1.get())
        n2 = int(self.caixa_2.get())
        self.resutado['text'] = n1 - n2

    def multiplicar(self):
        n1 = int(self.caixa_1.get())
        n2 = int(self.caixa_2.get())
        self.resutado['text'] = n1 * n2

    def dividir(self):
        n1 = int(self.caixa_1.get())
        n2 = int(self.caixa_2.get())
        self.resutado['text'] = n1 / n2

    def limpar(self):
        self.caixa_1.delete(0)
        self.caixa_2.delete(0)
        self.resutado['text'] = " "

    def sair(self):
        self.janela.quit()



operacao = Calculadora()
