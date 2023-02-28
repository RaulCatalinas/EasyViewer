"""Crea un boton en la posicion y funcion a ejecutar deseada"""

from tkinter import Button
from tkinter.font import Font

from cambiar_color import CambiarColor as color


class Boton(Button):
    """
    Crea un botón.

    :param texto: El texto que se mostrará en el botón
    :param posicion_eje_x: La posición x del botón
    :param ancho: ancho
    :param color_fondo: El color de fondo del botón
    :param funcion: La función a la que llamará el botón cuando se haga clic en él
    :param ventana: La ventana en la que estará el botón
    :param color_raton_dentro: El color del botón cuando el mouse está sobre él
    :param color_raton_fuera: El color del botón cuando el mouse no está sobre él
    :param posicion_absoluta: Si es Verdadero, el botón se colocará en la ventana utilizando el
    método pack(). Si es False, se colocará usando el método place()
    :param posicion_eje_y: La posición y del botón
    """

    def __init__(
        self,
        texto,
        ancho,
        color_fondo,
        funcion,
        ventana,
        color_raton_dentro,
        color_raton_fuera,
        posicion_absoluta,
        fuente,
        tamaño_fuente,
        posicion_eje_x=None,
        posicion_eje_y=None,
    ):
        self.texto = texto
        self.ancho = ancho
        self.color_fondo = color_fondo
        self.ventana = ventana
        self.color_raton_dentro = color_raton_dentro
        self.color_raton_fuera = color_raton_fuera
        self.funcion = funcion
        self.posicion_absoluta = posicion_absoluta
        self.posicion_eje_x = posicion_eje_x
        self.posicion_eje_y = posicion_eje_y
        self.fuente = fuente
        self.tamaño_fuente = tamaño_fuente

        super().__init__(
            self.ventana,
            text=self.texto,
            bg=self.color_fondo,
            font=Font(family=self.fuente, size=self.tamaño_fuente),
            command=self.funcion,
            width=self.ancho,
        )

        if self.posicion_absoluta:
            self.pack(pady=self.posicion_eje_y)
        else:
            self.place(x=self.posicion_eje_x, y=self.posicion_eje_y)

        color.hover(
            self,
            self.color_raton_dentro,
            self.color_raton_fuera,
        )

    def desactivar(self):
        """
        Deshabilita el botón
        """
        self.configure(state="disabled")

    def activar(self):
        """
        Habilita el botón
        """
        self.configure(state="normal")

    def config_boton(self, nuevo_texto):
        """
        Toma una cadena como argumento y cambia el texto del botón a esa cadena

        :param nuevo_texto: El nuevo texto que se mostrará en el botón
        """
        self.configure(text=nuevo_texto)
