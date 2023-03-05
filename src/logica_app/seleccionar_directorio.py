"""Solicita al usuario que seleccione un directorio para el archivo descargado"""

from tkinter.filedialog import askdirectory


class SeleccionarDirectorio:
    """Controla la logica que selecciona uun directorio para el video"""

    def __init__(self, ubicacion_video):
        self.ubicacion_video = ubicacion_video

        return self.ubicacion_video.set(
            askdirectory(initialdir="Directorio seleccionado")
        )
