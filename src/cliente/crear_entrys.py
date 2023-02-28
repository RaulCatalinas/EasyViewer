"""Crea los entrys para que el usuario interactue con la app"""

from tkinter import Entry
from tkinter.font import Font


class CrearEntrys(Entry):
    """Esta función crea un widget de Entrada y lo posiciona en la ventana."""

    def __init__(
        self, ventana, textvariable, fuente, tamaño_fuente, ancho, posicion_eje_y
    ):
        self.ventana = ventana
        self.textvariable = textvariable
        self.fuente = fuente
        self.tamaño_fuente = tamaño_fuente
        self.ancho = ancho
        self.posicion_eje_y = posicion_eje_y

        # Crear el Entry
        super().__init__(
            self.ventana,
            textvariable=self.textvariable,
            font=Font(family=self.fuente, size=self.tamaño_fuente),
            width=self.ancho,
        )
        # Posicionar el Entry
        self.pack(pady=self.posicion_eje_y)

    def desactivar(self):
        """
        Deshabilita el widget de entrada.
        """
        self.config(state="disabled")

    def activar(self):
        """
        Cambia el estado del widget de entrada a normal.
        """
        self.config(state="normal")
