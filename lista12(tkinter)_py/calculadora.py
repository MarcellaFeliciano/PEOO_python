from tkinter import *

class Calculadora:
    def __init__(self):
        self.janela = Tk()
        self.tela()
        #self.frames_tela()
        self.img_ifrn()
        self.widgets()
    
        self.janela.mainloop()

    def tela(self):
        self.janela.title('Calculadora')
        self.janela.geometry('320x280')

        self.canvas = Canvas(self.janela, bg='gray', height=280, width=320)
        self.canvas.pack()

    #def frames_tela(self):
        #self.frame1 = Frame(self.janela, height=80, width=320, bg='black' )
        #self.frame1.pack()

    def img_ifrn(self):
        self.imagem_ifrn = PhotoImage(file='logo_ifrn_01.png').subsample(13)
        self.imagemExibida = self.canvas.create_image(45,50,image=self.imagem_ifrn)

        self.canvas.tag_bind(self.imagemExibida,'<Button>',self.mudar_cor)
        
    def widgets(self):

        self.tela_resu = Label(self.canvas, text='0.00', bg='white', font=('Arial','16','bold'), width=16, height=3, anchor="e", justify=RIGHT)
        self.tela_resu.place(x=90,y=13)


        self.bt_0 = Button(self.canvas, text='0', width=6, height=1, bg='lightgrey', font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_0['command'] = lambda: self.numero("0")
        self.bt_0.place(x=14, y=210)

        self.bt_1 = Button(self.canvas, text='1', width=6, height=1, bg='lightgrey', font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_1['command'] = lambda: self.numero("1")
        self.bt_1.place(x=14, y=178)

        self.bt_2 = Button(self.canvas, text='2', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_2['command'] = lambda: self.numero("2")
        self.bt_2.place(x=74, y=178)

        self.bt_3 = Button(self.canvas, text='3', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_3['command'] = lambda: self.numero("3")
        self.bt_3.place(x=134, y=178)

        self.bt_4 = Button(self.canvas, text='4', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_4['command'] = lambda: self.numero("4")
        self.bt_4.place(x=14, y=146)

        self.bt_5 = Button(self.canvas, text='5', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_5['command'] = lambda: self.numero("5")
        self.bt_5.place(x=74, y=146)

        self.bt_6 = Button(self.canvas, text='6', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_6['command'] = lambda: self.numero("6")
        self.bt_6.place(x=134, y=146)

        self.bt_7 = Button(self.canvas, text='7', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_7['command'] = lambda: self.numero("7")
        self.bt_7.place(x=14, y=114)

        self.bt_8 = Button(self.canvas, text='8', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_8['command'] = lambda: self.numero("8")
        self.bt_8.place(x=74, y=114)

        self.bt_9 = Button(self.canvas, text='9', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_9['command'] = lambda: self.numero("9")
        self.bt_9.place(x=134, y=114)

        self.bt_ponto = Button(self.canvas, text='.', width=6, height=1, bg='lightgrey',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_ponto['command'] = lambda: self.numero(".")
        self.bt_ponto.place(x=74, y=210)

        self.bt_c = Button(self.canvas, command=self.limpar, text='C', width=6, height=1, bg='yellow',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_c.place(x=134, y=210)

        self.bt_soma = Button(self.canvas, text='+', width=6, height=1, bg='white',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_soma['command'] = lambda: self.numero("+")
        self.bt_soma.place(x=194, y=114)

        self.bt_subt = Button(self.canvas, text='-', width=6, height=1, bg='white',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_subt['command'] = lambda: self.numero("-")
        self.bt_subt.place(x=194, y=146)

        self.bt_div = Button(self.canvas, text='/', width=6, height=1, bg='white',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_div['command'] = lambda: self.numero("/")
        self.bt_div.place(x=194, y=178)

        self.bt_mult = Button(self.canvas, text='*', width=6, height=1, bg='white',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_mult['command'] = lambda: self.numero("*")
        self.bt_mult.place(x=194, y=210)

        self.bt_seta = Button(self.canvas, command=self.apagar, text='←', width=6, height=1, bg='red',font=('Arial','10','bold'), pady=1, bd=2)
        self.bt_seta.place(x=254, y=114)

        self.bt_igual = Button(self.canvas, command=self.resutado, text='=', width=6, height=5, bg='black',font=('Arial','10','bold'), pady=1, bd=2, fg='white')
        self.bt_igual.place(x=254, y=146)
              
        self.texto = self.canvas.create_text((270,260),text='Lista 12', fill='white', font=('Arial','14'))

    def limpar(self):
        self.tela_resu['text'] = ' '
        self.lista_n1 = []
        self.lista_n2 = []

    def apagar(self):
        string = self.tela_resu['text'].strip()
        self.tela_resu['text'] = string[:-1]

        if self.lista_n1 != []:
            if self.lista_n2 == []:
                self.lista_n1.pop(-1)

            else:
                self.lista_n2.pop()

        #valor = self.tela_resu['text'].replace(ultimo, " ")
        #self.tela_resu['text'] = valor 


    def mudar_cor(self, evento):

        if self.bt_igual['bg'] == 'black':
            self.bt_igual.configure(bg='blue')

        else:
            self.bt_igual.configure(bg='black')

    def numero(self, num):
    
        # adicionar os numeros a lista e mostrar is numeros na tela
        if self.tela_resu['text'] == '0.00' or self.tela_resu['text'] == ' ':
            self.lista_n1 = list()
            self.lista_n2 = list()

            self.lista_n1 = [num]

            # adicioanar os numeros a tela
            self.tela_resu['text'] = num
        
        else:
            if num in ['+','-','/','*']:

                self.p = int()
                for i in self.lista_n1:
                    if i in ['+','-','/','*']:
                        self.p = 1

                if self.p == 1:
                    pass

                else:
                    self.lista_n1.append(num)
                    # adicioanar os numeros a tela 
                    self.tela_resu['text'] += num
            
            else:
                self.p = int()
                for i in self.lista_n1:
                    if i in ['+','-','/','*']:
                        self.p = 1

                if self.p == 1:
                    self.lista_n2.append(num)
                    
                else:
                    self.lista_n1.append(num)

                print(self.lista_n1)
                print(self.lista_n2)
                # adicioanar os numeros a tela
                self.tela_resu['text'] += num


        # saber qual a operação
        if num in ['+','-','/','*']:
            if num  not in self.lista_n1:
                pass

            else:
                if num == '+':
                    self.operacao = 'soma'

                if num == '-':
                    self.operacao = 'subt'

                if num == '/':
                    self.operacao = 'div'

                if num == '*':
                    self.operacao = 'mult'
            print(self.operacao)

    def resutado(self):
        self.lista_n1 =  self.lista_n1[:-1]

        self.n1 = ""
        self.n2 = ""

        for i in self.lista_n1:
            self.n1 += i

        for i in self.lista_n2:
            self.n2 += i

        self.n1 = float(self.n1)
        self.n2 = float(self.n2)

        if self.operacao == 'soma':
            self.soma = self.n1+self.n2
            self.tela_resu['text'] = str(self.soma)

        elif self.operacao == 'subt':
            self.subt = self.n1 - self.n2
            self.tela_resu['text'] = str(self.subt)

        elif self.operacao == 'div':
            self.div = self.n1 / self.n2
            self.tela_resu['text'] = str(self.div)
        
        elif self.operacao == 'mult':
            self.mult = self.n1 * self.n2
            self.tela_resu['text'] = str(self.mult)

        self.lista_n1 = [self.tela_resu['text'].strip()]
        self.lista_n2 = []
        print(self.lista_n1)


        
iniciar = Calculadora()