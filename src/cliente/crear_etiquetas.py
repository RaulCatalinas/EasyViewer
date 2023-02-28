"""Crea los labels de la app"""

from tkinter import Label, font


class Etiqueta:
    """Crea los labels y los coloca en pantalla"""

    def __init__(
        self, texto, posicion_eje_y, ancho, color_fondo, fuente, tamaño_fuente, ventana
    ):
        # Crea una etiqueta con los parámetros dados
        self.texto = texto
        self.posicion_eje_y = posicion_eje_y
        self.ancho = ancho
        self.color_fondo = color_fondo
        self.fuente = fuente
        self.tamaño_fuente = tamaño_fuente
        self.ventana = ventana

        # Crear la etiqueta
        self.etiqueta = Label(
            self.ventana,
            text=self.texto,
            font=font.Font(family=self.fuente, size=self.tamaño_fuente),
            width=self.ancho,
            bg=self.color_fondo,
        )

        # Colocar la etiqueta en la ventana
        self.etiqueta.pack(pady=self.posicion_eje_y)

    def config_etiqueta(self, nuevo_texto):
        """Cambia el texto del label por el nuevo_texto"""
        self.etiqueta.configure(text=nuevo_texto)
