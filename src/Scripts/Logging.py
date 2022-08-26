from logging import DEBUG, info, basicConfig, error
from os import chdir
from os.path import dirname

from Log.Log import getLog


# Configurar el logging
class GestionLogging:
    def __init__(self):
        basicConfig(
            level=DEBUG,
            filename=getLog(),
            filemode="w",
        )
        chdir(dirname(__file__))

    @staticmethod
    def writeLog(mensaje):
        info(mensaje)

    @staticmethod
    def writeError(mensaje):
        error(mensaje)
