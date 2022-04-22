from game import GameTimer
import tkinter
from tkinter import messagebox


class TelaDoJogo(object):
    """
    Classe que inicia a tela do jogo e carrega as funções de frases,
    timer.
    """

    def __init__(self):
        # Tela de Jogo com Tamanho e Titulo
        self.root = tkinter.Tk()
        self.root.geometry("1280x760")
        self.root.title("Type Game")

        # Botões da Tela de Jogo
        self.buttonStart =tkinter.Button(self.root, text="Começar", bd="8", command=None)
        self.buttonStart.place(x = 640, y  = 600)

        # Roda o game enquanto a tela não é fechada
        self.root.mainloop()


tela = TelaDoJogo()