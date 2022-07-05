from datetime import datetime
from logging import DEBUG, info, basicConfig, error


# Configurar el logging
class GestionLogging:
    def __init__(self):
        self.__ConfigurarLogging()

        info(
            f"El programa Descargador de videos de YouTube se ha ejecutado el {self.__getFecha()}"
        )

    @staticmethod
    def __getFecha():
        fecha = datetime.today()
        formato = fecha.strftime("%A, %d %B, %Y %H:%M")
        return formato

    @staticmethod
    def __ConfigurarLogging():
        basicConfig(filename="./Log/YoutubeDownloader.log", filemode="w", level=DEBUG)

    @staticmethod
    def writeLog(mensaje):
        info(mensaje)

    @staticmethod
    def writeError(mensaje):
        error(mensaje)
