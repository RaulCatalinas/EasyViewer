from os.path import isdir
from platform import system
from subprocess import call

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


def __ping(host):
    """
    Comprueba si el host está activo
    """
    parametro = "-n" if system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "4", host]
    return call(comando)


def Comprobar_Conexion_Internet(log):
    """
    Comprueba si hay conexión a internet
    """
    try:
        __ping("google.com")
        log.writeLog("Conexión a internet establecida")
        return True
    except:
        log.writeError("No hay conexión a internet")
        raise Exception("No hay conexión a internet")
    finally:
        log.writeLog("Comprobación de conexión a internet finalizada")
