# Crear una clase que se encarga de crear una ventana heredando de la clase Tk
from os import chdir
from os.path import dirname
from tkinter import Tk, PhotoImage

from src.Icon import Icono


class Ventana(Tk):
    def __init__(self, colorDeFondo, tituloVentana, ancho, alto):
        self.colorDeFondo = colorDeFondo
        self.tituloVentana = tituloVentana
        self.ancho = ancho
        self.alto = alto
        super().__init__()
        self.title(self.tituloVentana)
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file=Icono.getIcono()))
        chdir(dirname(__file__))
        self.config(bg=self.colorDeFondo)

    def ActualizarVentana(self):
        self.mainloop()
