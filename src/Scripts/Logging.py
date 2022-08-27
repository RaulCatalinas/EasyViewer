from logging import DEBUG, info, basicConfig, error
from os import mkdir
from os.path import exists


# Configurar el logging
class GestionLogging:
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
    def writeLog(mensaje):
        info(mensaje)

    @staticmethod
    def writeError(mensaje):
        error(mensaje)
