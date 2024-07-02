

def aumentarVolume():
    print("Volume Aumentou")

def diminuirVolume():
    print("Volume Diminuiu")


def ligaTV():
    televisao = Toplevel(controle)
    televisao.title("TV")
    canal2 = PhotoImage(file="rc.gif")
    exibir_imagem = Label(televisao, image=canal2)
    exibir_imagem.image = canal2
    exibir_imagem.pack()