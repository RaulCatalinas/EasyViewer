"""Muestra el progreso de la descarga"""

from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar


class BarraDeProgresion:
    """Crea una barra de progreso y aumenta el progrso de ella"""

    def __init__(
        self,
        ventana,
        posicion_eje_x,
        posicion_eje_y,
    ):
        self.ventana = ventana
        self.posicion_eje_x = posicion_eje_x
        self.posicion_eje_y = posicion_eje_y
        self.barra_progresion_descarga = Progressbar(
            self.ventana, orient=HORIZONTAL, length=800
        )
        self.barra_progresion_descarga.place(
            x=self.posicion_eje_x, y=self.posicion_eje_y
        )

    def ejecutar_barra_de_progresion(self):
        """
        Inicia una barra de progreso.
        """
        self.barra_progresion_descarga.start()

    def detener_barra_de_progresion(self):
        """
        Detiene la barra de progreso.
        """
        self.barra_progresion_descarga.stop()
