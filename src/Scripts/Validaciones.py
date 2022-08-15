from os.path import isdir

from pytube import YouTube
from requests import get, ConnectionError, Timeout


def Comprobar_Si_Se_Ha_Seleccionado_Directorio(Directorio_Descarga, log):
    """
    Comprueba si se ha seleccionado un directorio
    """

    if isdir(Directorio_Descarga.get()):
        log.writeLog("Se ha seleccionado ningún directorio para guardar el video")
        return True
    else:
        raise Exception("No se ha seleccionado ningún directorio")
        log.writeError("No se ha seleccionado ningún directorio")


def Comprobar_Si_Es_URL_YouTube(url, log):
    """
    Comprueba si la URL es de YouTube
    """
    if "https://www.youtube.com/watch?v=" in url or "https://youtu.be/" in url:
        log.writeLog("La URL es de YouTube")
        return True
    else:
        log.writeError("La URL no es de YouTube")
        raise Exception("La URL no es de YouTube")


def Comprobar_Conexion_Internet(log):
    """
    Comprueba si hay conexión a internet
    """
    try:
        get("https://www.google.es", timeout=5)
    except (ConnectionError, Timeout):
        raise Exception("No hay conexión a internet")
    else:
        log.writeLog("Ok, hay conexión a internet")
        return True


def Comprobar_Si_Se_Ha_Introducido_Una_URL(url, log):
    """
    Comprueba si se ha introducido una URL
    """
    if url == "":
        log.writeError("No se ha introducido ninguna URL")
        raise Exception("No se ha introducido ninguna URL")
    else:
        log.writeLog("Se ha introducido una URL")
        return True


def Comprobar_Si_El_Video_Esta_Disponible(log, URL_VIDEO):
    """
    Comprueba si el video está disponible
    """
    try:
        YouTube(URL_VIDEO).check_availability()
        log.writeLog("Ok, video disponible")
        return True

    except:
        log.writeError("No se ha podido acceder al video")
        raise Exception("No se ha podido acceder al video")