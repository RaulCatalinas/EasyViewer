"""Crea una barra de tareas"""

from tkinter import Menu
from webbrowser import open_new_tab

from get_config import Config

config = Config()


class BarraDeTareas:
    """Crea una barra de menú con dos menús, uno para redes sociales y otro para idioma"""

    def __init__(self, ventana, actualizar_texto_widgets):
        self.ventana = ventana
        self.actualizar_texto_widgets = actualizar_texto_widgets

        self.barra_de_tareas = Menu(self.ventana, tearoff=False)

        self.contacto = Menu(self.barra_de_tareas, tearoff=False)
        self.contacto.add_command(command=self.instagram, label="Instagram")
        self.contacto.add_command(command=self.twitter, label="Twitter")
        self.contacto.add_command(command=self.facebook, label="Facebook")

        self.idioma = Menu(self.barra_de_tareas, tearoff=False)
        self.idioma.add_command(
            label=config.get_config_execel(numero_columna_excel=13),
            command=self.español,
        )

        self.idioma.add_command(
            label=config.get_config_execel(numero_columna_excel=14),
            command=self.english,
        )

        self.barra_de_tareas.add_cascade(
            menu=self.contacto, label=config.get_config_execel(numero_columna_excel=11)
        )
        self.barra_de_tareas.add_cascade(
            menu=self.idioma, label=config.get_config_execel(numero_columna_excel=12)
        )

        self.ventana.config(menu=self.barra_de_tareas)

    @staticmethod
    def instagram():
        """
        Abre una nueva pestaña en su navegador y navega a la página de Instagram del usuario que
        especifique
        """
        open_new_tab("https://www.instagram.com/raulf1foreveryt_oficial/?hl=es")

    @staticmethod
    def twitter():
        """
        Abre una nueva pestaña en su navegador y va al instagram del autor de este código.
        """
        open_new_tab("https://twitter.com/F1foreverRaul")

    @staticmethod
    def facebook():
        """
        Abre una nueva pestaña en su navegador y va a la página de Facebook del autor de este código.
        """
        open_new_tab("https://www.facebook.com/Raul-F1forever-114186780454598/")

    def english(self):
        """
        Establece el idioma en inglés.
        """
        config.set_idioma("English")
        self.actualizar_texto_widgets()
        self.actualizar_texto_barra_de_tareas()

    def español(self):
        """
        Establece el idioma en español.
        """
        config.set_idioma("Español")
        self.actualizar_texto_widgets()
        self.actualizar_texto_barra_de_tareas()

    def actualizar_texto_barra_de_tareas(self):
        """
        Actualiza el texto de la barra de menú y el texto de la barra de tareas.
        """
        self.idioma.entryconfig(
            0,
            label=config.get_config_execel(numero_columna_excel=13),
        )
        self.idioma.entryconfig(
            1,
            label=config.get_config_execel(numero_columna_excel=14),
        )
        self.barra_de_tareas.entryconfig(
            0, label=config.get_config_execel(numero_columna_excel=11)
        )
        self.barra_de_tareas.entryconfig(
            1,
            label=config.get_config_execel(numero_columna_excel=12),
        )
