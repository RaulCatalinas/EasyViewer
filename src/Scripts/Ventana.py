# Crear una clase que se encarga de crear una ventana heredando de la clase Tk
from os import chdir
from os.path import dirname
from tkinter import Tk

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
        self.iconbitmap(Icono.getIcono())
        chdir(dirname(__file__))
        self.config(bg=self.colorDeFondo)

        self.__CentrarVentana()

    def ActualizarVentana(self):
        self.mainloop()

    def __CentrarVentana(self):
        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.winfo_screenwidth()
        Alto_Ventana = self.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (self.ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (self.alto / 2))

        # Redimensionar Ventana
        return self.geometry(
            "{}x{}+{}+{}".format(self.ancho, self.alto, Coordenada_X, Coordenada_Y)
        )
