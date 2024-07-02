from tkinter import *
import pickle

class App:
    def __init__(self):
        self.tela()
        self.widgets()
        self.registro_agenda = dict()
        self.janela.mainloop()

    def tela(self):
        self.janela = Tk()
        self.janela.geometry('790x400')
        self.janela.title('030 - Serialização e Persistência')

        self.canvas1 = Canvas(self.janela, width=790, height=400)
        self.canvas1.pack()


    def widgets(self):

        self.titulo1 = Label(self.canvas1,text='Agenda Internacional', width=52, height=2, bg='black', font='Arial 20 bold', fg='white', borderwidth=5, relief='raised',)
        self.titulo1.place(x=0,y=0)

        self.canvas1.create_line(550,1, 550,400, dash = (5,2))

        self.canvas1.create_rectangle(10,337, 540,390)

        
        self.tituloLeitura = Label(self.canvas1,width=24,fg='blue',text='Leitura/Desserialização',bg='white',font='Helvetica 12')
        self.tituloLeitura.place(x=560,y=80)

        self.textoNome1 = Label(self.canvas1,text='Nome do Arquivo: ',font='Helvetica 15')
        self.textoNome1.place(x=560,y=110)

        self.nome_arquivo1 = Entry(self.canvas1,width=21,font='Helvetica 14')
        self.nome_arquivo1.place(x=560,y=140)

        self.BotaoLer = Button(self.canvas1, command=self.disserializar, width=20,text='Ler/Desserializar',bg='blue',fg='white',font='Helvetica 14')
        self.BotaoLer.place(x=560,y=180)

        self.canvas1.create_line(550,233,785,233,dash = (5,2))

        self.tituloGravacao = Label(self.canvas1,width=24,fg='red',text='Serialização/Persistência',bg='white', font='Helvetica 12')
        self.tituloGravacao.place(x=560,y=250)

        self.textoNome2 = Label(self.canvas1,text='Nome do Arquivo: ',font='Helvetica 15' )
        self.textoNome2.place(x=560,y=280)

        self.nome_arquivo2= Entry(self.canvas1,width=21,font='Helvetica 14')
        self.nome_arquivo2.place(x=560,y=310)

        self.botaoGravar = Button(self.canvas1, command=self.serializar, width=20,text='Serializar/Gravar',bg='red',fg='white',font='Helvetica 14')
        self.botaoGravar.place(x=560,y=350)

        self.botaoModoInclusao = Button(self.canvas1, command=self.habilitaInclusao, text='Modo Inclusão',width=26,height=2)
        self.botaoModoInclusao.place(x=16,y=340)

        self.botaoModoConsulta = Button(self.canvas1, command = self.habilitaConsulta, text='Modo Consulta',width=25,height=2)
        self.botaoModoConsulta.place(x=283,y=340)


        self.textoNomeAgenda = Label(self.canvas1,text='Nome:',font='Helvetica 14 bold')
        self.textoNomeAgenda.place(x=20,y=100)

        self.caixaNomeAgenda = Entry(self.canvas1,font='Helvetica 14 bold')
        self.caixaNomeAgenda.place(x=20,y=135,height=40,width=510)

        self.textoTelefoneAgenda = Label(self.canvas1,text='Telefone:',font='Helvetica 14 bold')
        self.textoTelefoneAgenda.place(x=20,y=190)

        self.caixaTelefoneAgenda = Entry(self.canvas1,font='Helvetica 14 bold')
        self.caixaTelefoneAgenda.place(x=20,y=225,height=40,width=510)


        self.botaoInserir = Button(self.canvas1, command=self.inserir, text='Inserir',font='Helvetica 12 bold',width=17,height=2,bg='green',bd=3,fg='white',)
        self.botaoInserir.place(x=327,y=273)



    def habilitaConsulta(self):

        self.caixaNomeAgenda.delete(0,END)

        self.labelTelefoneAgenda = Label(self.canvas1,font='Helvetica 14 bold',fg='blue',anchor='w')
        self.labelTelefoneAgenda.place(x=20,y=225,height=40,width=510)

        self.botaoConsultar = Button(self.canvas1, command=self.consultar_registro, text='Consultar',font='Helvetica 12 bold',width=17,height=2,bg='blue',bd=3,fg='white' )
        self.botaoConsultar.place(x=327,y=273)



    def habilitaInclusao(self):

        self.caixaNomeAgenda = Entry(self.canvas1,font='Helvetica 14 bold')
        self.caixaNomeAgenda.place(x=20,y=135,height=40,width=510)

        self.caixaTelefoneAgenda = Entry(self.canvas1,font='Helvetica 14 bold')
        self.caixaTelefoneAgenda.place(x=20,y=225,height=40,width=510)

        self.botaoInserir = Button(self.canvas1, command=self.inserir, text='Inserir',font='Helvetica 12 bold',width=17,height=2,bg='green',bd=3,fg='white')
        self.botaoInserir.place(x=327,y=273)

    def inserir(self):
        self.nome = self.caixaNomeAgenda.get()
        self.telefone = self.caixaTelefoneAgenda.get()
        self.registro_agenda.update({self.nome : self.telefone})
        print(self.registro_agenda)

    def serializar(self):
        arq = open(self.nome_arquivo2.get(), 'wb')
        pickle.dump(self.registro_agenda, arq)
        arq.close()

    def disserializar(self):
        arq = open(self.nome_arquivo1.get(),'rb')
        self.registro_disserializado = pickle.load(arq)
        arq.close()


    def consultar_registro(self):
        self.nome_registro = self.caixaNomeAgenda.get()
        self.chave_registro = self.registro_agenda.keys()

        if self.nome_registro in self.chave_registro:
            print(self.registro_agenda[self.nome_registro])
            self.caixaTelefoneAgenda = Label(self.canvas1, text=f'{self.registro_agenda[self.nome_registro]}', font='Helvetia 14 bold')
        else:
            self.caixaTelefoneAgenda = Label(self.canvas1, text='Registro Não Encontrado', font='Helvetia 14 bold')

        self.caixaTelefoneAgenda.place(x=20, y=225)



aplicacao=App()