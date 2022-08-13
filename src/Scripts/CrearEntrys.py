from tkinter import Entry


# Clase que se encarga de crear los Entrys
class CrearEntrys:
    def __init__(self, ventana, textvariable, fuente, tamañoDeFuente, ancho, y):
        """
        Esta función crea un widget de Entrada y lo posiciona en la ventana.
        @param ventana - La ventana donde se colocará la Entrada.
        @param textvariable - Esta es la variable que se utilizará para almacenar el texto que ingresa el usuario.
        @param fuente - La fuente que desea utilizar.
        @param tamañoDeFuente - El tamaño de fuente del texto en la Entrada.
        @param ancho - ancho de la entrada
        @param y - La posición del eje Y de la entrada.
        """
        self.ventana = ventana
        self.textvariable = textvariable
        self.fuente = fuente
        self.tamañoDeFuente = tamañoDeFuente
        self.ancho = ancho
        self.y = y

        # Crear el Entry
        self.crearEntry = Entry(
            self.ventana,
            textvariable=self.textvariable,
            font=(self.fuente, self.tamañoDeFuente),
            width=self.ancho,
        )

        # Posicionar el Entry
        self.crearEntry.pack(pady=self.y)
