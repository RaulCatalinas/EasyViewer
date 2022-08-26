from tkinter.filedialog import askdirectory

from Logging import GestionLogging

log = GestionLogging()


# Clase que se encarga de preguntar al usuario donde quiere guardar el video
class Buscar:
    def __init__(self, UBICACION_VIDEO):
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.Directorio_Descarga = None

    def FuncionBuscar(self):
        """
        Abre un cuadro de diálogo de archivo y establece el valor de la variable “Ubicacion_Video_PC” al directorio
        seleccionado por el usuario
        """

        log.writeLog(
            "Se ha hecho click en el botón de seleccionar la ubicacion donde se guardara el video y/o el audio del video"
        )
        self.Directorio_Descarga = askdirectory(initialdir="Directorio seleccionado")
        self.UBICACION_VIDEO.set(self.Directorio_Descarga)
