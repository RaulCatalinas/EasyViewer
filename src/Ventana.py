# Crear una clase que se encarga de crear una ventana heredando de la clase Tk
from os import chdir
from os.path import dirname
from tkinter import Tk, PhotoImage

from Icon.Icono import getIcono


class Ventana(Tk):
    def __init__(self, colorDeFondo, tituloVentana, ancho, alto):
        self.colorDeFondo = colorDeFondo
        self.tituloVentana = tituloVentana
        self.ancho = ancho
        self.alto = alto
        super().__init__()
        self.title(self.tituloVentana)

        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.winfo_screenwidth()
        Alto_Ventana = self.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (alto / 2))

        # Redimensionar Ventana
        self.geometry("{}x{}+{}+{}".format(ancho, alto, Coordenada_X, Coordenada_Y))

        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file=getIcono()))
        chdir(dirname(__file__))
        self.config(bg=self.colorDeFondo)

    def ActualizarVentana(self):
        self.mainloop()
