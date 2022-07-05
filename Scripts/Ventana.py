# Crear una clase que se encarga de crear una ventana heredando de la clase Tk
from tkinter import Tk
from Scripts.CambiarColor import colores as color


class Ventana(Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Downloader")
        self.resizable(False, False)
        self.iconbitmap(".\Icon\Icono.ico")
        self.config(bg=color["Negro"])

        # Medida ventana
        Ancho = 830
        Alto = 520

        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.winfo_screenwidth()
        Alto_Ventana = self.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (Ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (Alto / 2))

        # Redimensionar Ventana
        self.geometry("{}x{}+{}+{}".format(Ancho, Alto, Coordenada_X, Coordenada_Y))

    def ActualizarVentana(self):
        self.mainloop()
