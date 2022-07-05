from tkinter import Label


# Clase que crea los labels y los coloca en pantalla
class Etiqueta:
    def __init__(self, texto, y, ancho, colorFondo, fuente, tamañoFuente, ventana):
        """
        Crea una etiqueta con los parámetros dados y luego la coloca en la ventana.
        @param texto - El texto que se mostrará en la etiqueta.
        @param y - La posición del eje y de la etiqueta.
        @param ancho - El ancho de la etiqueta.
        @param colorFondo - El color de fondo de la etiqueta.
        @param fuente - La fuente a utilizar.
        @param tamañoFuente - Tamaño de la fuente.
        """
        # Crea una etiqueta con los parámetros dados
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana

        # Crear la etiqueta
        self.etiqueta = Label(
            self.ventana,
            text=self.texto,
            font=(self.fuente, self.tamañoFuente),
            width=self.ancho,
            bg=self.colorFondo,
        )
        # Colocar la etiqueta en la ventana
        self.etiqueta.pack(pady=self.y)
