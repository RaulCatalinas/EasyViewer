"""Solicita al usuario que seleccione un directorio para el archivo descargado"""

from tkinter.filedialog import askdirectory

from logging_app import GestionLogging

log = GestionLogging()


def seleccionar_directorio(ubicacion_video):
    """
    El usuario selecciona directorio para guaradar el archivo descargado
    """

    log.write_log("Se ha hecho click en el botón de seleccionar un directorio")

    _directorio_descarga = askdirectory(initialdir="Directorio seleccionado")
    return ubicacion_video.set(_directorio_descarga)
