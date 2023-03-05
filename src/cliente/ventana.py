"""Crea la GUI de la app"""

from tkinter import Tk, PhotoImage


class Ventana(Tk):
    """Crea la ventana principal del la app"""

    def __init__(self, color_fondo, titulo_ventana, ancho, alto, icono=None):
        self.color_fondo = color_fondo
        self.titulo_ventana = titulo_ventana
        self.ancho = ancho
        self.alto = alto
        self.icono = icono
        super().__init__(useTk=True)
        self.title(self.titulo_ventana)

        # Cálculos para el centrado de la ventana
        ancho_ventana = self.winfo_screenwidth()
        alto_ventana = self.winfo_screenheight()

        coordenada_x = int((ancho_ventana / 2) - (ancho / 2))
        coordenada_y = int((alto_ventana / 2) - (alto / 2))

        # Redimensionar Ventana
        self.geometry(f"{ancho}x{alto}+{coordenada_x}+{ coordenada_y}")

        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file=self.icono))
        self.config(bg=self.color_fondo)

    def actualizar_ventana(self):
        """
        Actualiza la ventana.
        """
        self.mainloop()
