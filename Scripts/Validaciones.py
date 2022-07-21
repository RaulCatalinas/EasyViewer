from os.path import isdir

from pytube.exceptions import VideoPrivate, VideoUnavailable
from pytube.request import get


def Comprobar_Si_Se_Ha_Seleccionado_Directorio(Directorio_Descarga, log, showerror):
    """
    Comprueba si se ha seleccionado un directorio
    """

    if isdir(Directorio_Descarga.get()):
        log.writeLog(
            "Se ha seleccionado ningún directorio para guardar el video"
        )
        return True
    else:
        showerror(
            "Error de directorio",
            "No se ha seleccionado ningún directorio",
        )
        log.writeError(
            "No se ha seleccionado un directorio para guardar el video"
        )
        return False


def Comprobar_Si_Es_URL_YouTube(url, log):
    """
    Comprueba si la URL es de YouTube
    """
    try:
        if get(url):
            return True
    except VideoPrivate:
        log.writeError("El video es privado")
        raise Exception("El video es privado")
    except VideoUnavailable:
        log.writeError("El video no está disponible")
        raise Exception("El video no está disponible")
    except:
        log.writeError("La URL no es de YouTube")
        raise Exception("La url no es de youtube")
