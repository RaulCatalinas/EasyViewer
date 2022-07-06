from tkinter.filedialog import askdirectory


# Clase que se encarga de preguntar al usuario donde quiere guardar el video
class Buscar:
    def __init__(self, UBICACION_VIDEO, log):
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.Directorio_Descarga = None
        self.log = log

    def FuncionBuscar(self):
        """
        Abre un cuadro de diálogo de archivo y establece el valor de la variable “Ubicacion_Video_PC” al directorio
        seleccionado por el usuario
        """

        self.log.writeLog(
            "Se ha hecho click en el botón de seleccionar la dirección de la carpeta donde se quiere "
            "guardar el video descargado"
        )
        self.Directorio_Descarga = askdirectory(initialdir="Directorio seleccionado")
        self.UBICACION_VIDEO.set(self.Directorio_Descarga)
