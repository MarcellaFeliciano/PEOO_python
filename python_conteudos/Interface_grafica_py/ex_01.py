from tkinter import *


janela = Tk()
janela.title('Minha Primeira Janela <3')
janela.geometry('400x300')

# O texto (rotulo) da pagina!
# label = Label(janela, text='Olá,Mundo!!!', font= (Courier 20))
#(pady = 70) não é obrigatorio
# label.pack(pady = 70) - padding

#



botao = Button(janela, text='Ops')
botao.pack(pady = 70)

janela.mainloop()
botao.mainloop()
