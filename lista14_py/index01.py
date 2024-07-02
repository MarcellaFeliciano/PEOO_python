from tkinter import *
import requests, json


class App:
    def __init__(self):
        self.tela()
        self.widgets()
        self.janela.mainloop()

    """ 
        def banco_dados(self):
            conection = sqlite3.connect('banco.db')
            sql = conection.cursor()
            sql.execute('CREATE TABLE dataset (razão_social, nome_fantasia, municipio, estado)')

            #conection.commit()
            #conection.close() 
    """
    
    def tela(self):
        self.janela = Tk()
        self.janela.title('Lista 12 - Questão 01')
        self.janela.geometry("460x390")
        self.janela.resizable(width = False, height = False)



    def widgets(self):
        self.Label1 = Label(background = 'white', foreground = 'black', font = 'Arial 14 bold', text = 'Consulta Informações de Pessoa Jurídica CNPJ ', )
        self.Label1.place(x = 2, y = 5, height = 43, width = 456, anchor = 'nw')

        self.Label2 = Label(font = 'Arial 14 bold', text = 'Informe CNPJ a consultar:', )
        self.Label2.place(x = 7, y = 60, height = 30, width = 236, anchor = 'nw')

        self.Entry1 = Entry(font = 'Arial 16 bold', foreground = 'blue')
        self.Entry1.place(x = 248, y = 57, height = 38, width = 201, anchor = 'nw')

        self.Button1 = Button(font = 'Arial 16 bold', command=self.consultar, background = 'blue', foreground = 'white', text = 'Consultar CNPJ', )
        self.Button1.place(x = 10, y = 117, height = 37, width = 440, anchor = 'nw')

        self.Label3 = Label(anchor = 'w', text = 'Razão Social:', )
        self.Label3.place(x = 8, y = 188, height = 30, width = 101, anchor = 'nw')

        self.Label4 = Label(anchor = 'w', background = '#adadad', text = 'resposta ', )
        self.Label4.place(x = 448, y = 186, height = 30, width = 344, anchor = 'ne')

        self.Label5 = Label(anchor = 'w', text = 'Nome Fantasia:', )
        self.Label5.place(x = 10, y = 229, height = 30, width = 113, anchor = 'nw')

        self.Label6 = Label(anchor = 'w', background = '#adadad', text = 'resposta ', )
        self.Label6.place(x = 449, y = 227, height = 30, width = 324, anchor = 'ne')

        self.Label7 = Label(anchor = 'w', text = 'Município:', )
        self.Label7.place(x = 13, y = 269, height = 30, width = 70, anchor = 'nw')

        self.Label8 = Label(anchor = 'w', background = '#adadad', text = 'resposta ', )
        self.Label8.place(x = 450, y = 268, height = 30, width = 358, anchor = 'ne')

        self.Label9 = Label(anchor = 'w', text = 'Estado UF :', )
        self.Label9.place(x = 12, y = 308, height = 30, width = 90, anchor = 'nw')

        self.Label10 = Label(anchor = 'w', background = '#adadad', text = 'resposta ', )
        self.Label10.place(x = 100, y = 309, height = 30, width = 350, anchor = 'nw')

        self.Label11 = Label(anchor = 'w', background = 'black', foreground = 'white', text = 'Situação:', )
        self.Label11.place(x = 10, y = 349, height = 30, width = 441, anchor = 'nw')

        


    def consultar(self):
        val_cnpj = self.Entry1.get()

        self.consulta = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{val_cnpj}')

        print(self.consulta)
        # 49672034000111

        if self.consulta.status_code != 200:
            self.Label11 = Label(anchor = 'w', background = 'red', foreground = 'white', text = 'Situação: CNPJ Inválido', )
            self.Label11.place(x = 10, y = 349, height = 30, width = 441, anchor = 'nw')
            
        else:       

            self.Label4 = Label(anchor = 'w', background = '#adadad', text = f'{self.consulta.json()["razao_social"]}', )
            self.Label4.place(x = 448, y = 186, height = 30, width = 344, anchor = 'ne')

            self.Label6 = Label(anchor = 'w', background = '#adadad', text = f'{self.consulta.json()["nome_fantasia"]}')
            self.Label6.place(x = 449, y = 227, height = 30, width = 324, anchor = 'ne')

            self.Label8 = Label(anchor = 'w', background = '#adadad', text = f'{self.consulta.json()["municipio"]}', )
            self.Label8.place(x = 450, y = 268, height = 30, width = 358, anchor = 'ne')

            self.Label10 = Label(anchor = 'w', background = '#adadad', text = f'{self.consulta.json()["uf"]}')
            self.Label10.place(x = 100, y = 309, height = 30, width = 350, anchor = 'nw')

            self.Label11 = Label(anchor = 'w', background = 'green', foreground = 'white', text = 'Situação: CNPJ Válido', )
            self.Label11.place(x = 10, y = 349, height = 30, width = 441, anchor = 'nw')


        



aplicacao=App()