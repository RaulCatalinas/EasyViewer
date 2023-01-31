"""Menu con las opciones de copiar y pegar"""

from tkinter import Menu

from pyperclip import copy, paste


class MenuDeOpciones:
    """Crea un menu de opciones para poder copiar y pegar la url del portapapeles"""
    def __init__(self, ventana, texto_a_copiar):
        self.ventana = ventana
        self.texto_a_copiar = texto_a_copiar
        self.menu = Menu(self.ventana, tearoff=0)
        self.menu.add_command(label="Copiar", command=self.__copiar)
        self.menu.add_command(label="Pegar", command=self.__pegar)

    def crear_menu_de_opciones(self, event):
        """
        Crea un menú de opciones.

        :param event: El evento que activó la ventana emergente
        """
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def __copiar(self):
        """
        Copia el texto del cuadro de texto al portapapeles.
        """
        copy(self.texto_a_copiar.get())

    def __pegar(self):
        """
        Pega el texto del portapapeles.
        """
        self.texto_a_copiar.set(paste())
