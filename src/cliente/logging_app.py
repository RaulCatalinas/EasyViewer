"""Administra los logs de la app"""

from logging import DEBUG, info, basicConfig, error
from os import mkdir
from os.path import exists



class GestionLogging:
    """Crea una carpeta llamada "Log" si no existe, luego crea un archivo de registro llamado "App.log" en esa carpeta y escribre en ese log cuando se llama a la funcion encargada de ello"""
    def __init__(self):

        if not exists("Log"):
            mkdir("Log")

        basicConfig(
            level=DEBUG,
            filemode="w+",
            filename="Log/App.log",
            format="%(asctime)s -> %(levelname)s: %(message)s",
        )

    @staticmethod
    def write_log(mensaje):
        """
        Escribe un mensaje de registro en el archivo de log.

        :param mensaje: El mensaje que se escribirá en el archivo de log
        """
        info(mensaje)

    @staticmethod
    def write_error(mensaje):
        """
        Escribe un mensaje de error en el archivo de log.

        :param mensaje: El mensaje que se escribirá en el archivo de log
        """
        error(mensaje)