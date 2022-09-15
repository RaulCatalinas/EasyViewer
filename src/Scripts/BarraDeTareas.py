from tkinter import Menu
from webbrowser import open_new_tab


class BarraDeTareas:
    def __init__(self, ventana):
        self.ventana = ventana

        self.barra_De_Tareas = Menu()

        self.contacto = Menu(self.barra_De_Tareas, tearoff=False)
        self.contacto.add_command(command=self.Instagram, label="Instagram")
        self.contacto.add_command(command=self.Twitter, label="Twitter")
        self.contacto.add_command(command=self.Facebook, label="Facebook")

        self.barra_De_Tareas.add_cascade(menu=self.contacto, label="Contacto")
        self.ventana.config(menu=self.barra_De_Tareas)

    @staticmethod
    def Instagram():
        open_new_tab("https://www.instagram.com/raulf1foreveryt_oficial/?hl=es")

    @staticmethod
    def Twitter():
        open_new_tab("https://twitter.com/F1foreverRaul")

    @staticmethod
    def Facebook():
        open_new_tab("https://www.facebook.com/Raul-F1forever-114186780454598/")
