from tkinter import * 
class Janela:
    def __init__(self, inicio):
        self.frame1 = Frame(inicio)
        self.frame1.pack()
        self.botao1 = Button(self.frame1, text='oi!', bg='yellow')
        self.botao1.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()
    
# - para ficar bonito -
# self.botao1 = Button(self.frame1) 
# self.butao1[text] = 'oiii!'
# self.butao1[bg] = 'yellowraiz = Tk()Janela(raiz)raiz.mainloop()