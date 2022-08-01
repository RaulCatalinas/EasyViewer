# Crear una clase que se encarga de crear una ventana heredando de la clase Tk
from os.path import abspath
from tkinter import Tk

icono = abspath("../Icon/Icono.ico")


class Ventana(Tk):
    def __init__(self, colorDeFondo):
        self.colorDeFondo = colorDeFondo
        super().__init__()
        self.title("Youtube Downloader")
        self.resizable(False, False)
        self.iconbitmap(icono)
        self.config(bg=self.colorDeFondo)

        self.__CentrarVentana()

    def ActualizarVentana(self):
        self.mainloop()

    def __CentrarVentana(self):
        # Medida ventana
        Ancho = 830
        Alto = 520

        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.winfo_screenwidth()
        Alto_Ventana = self.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (Ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (Alto / 2))

        # Redimensionar Ventana
        return self.geometry(
            "{}x{}+{}+{}".format(Ancho, Alto, Coordenada_X, Coordenada_Y)
        )
