from time import sleep
from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar


# Barra de progresión
class BarraDeProgresion:
    # Crear barra de progresion

    def __init__(
        self,
        ventana,
        PORCENTAJE_DESCARGA,
        PORCENTAJE_DESCARGA_STRING,
        x,
        y,
        tamañoArchivo=0,
    ):
        self.speed = None
        self.download = None
        self.GB = None
        self.ventana = ventana
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.PORCENTAJE_DESCARGA_STRING = PORCENTAJE_DESCARGA_STRING
        self.x = x
        self.y = y
        self.barraProgresionDescarga = Progressbar(
            self.ventana, orient=HORIZONTAL, length=800
        )
        self.barraProgresionDescarga.place(x=self.x, y=self.y)

    def AumentarProgreso(self):
        """
        Es una función que aumenta el valor de una barra de progreso en un 1% cada 0,09 segundos hasta llegar al 100%
        """
        self.GB = 0
        self.download = 0
        self.speed = 1
        while self.download < self.GB:
            sleep(0.09)
            self.barraProgresionDescarga["value"] += (self.speed / self.GB) * 100
            self.download += self.speed
            self.PORCENTAJE_DESCARGA.set(
                str(int((self.download / self.GB) * 100)) + "%"
            )
            self.PORCENTAJE_DESCARGA_STRING.set(
                str(self.download) + "/" + str(self.GB) + " files completed"
            )
            self.ventana.update_idletasks()
