from ctypes import windll, byref
from ctypes.wintypes import DWORD
from os.path import isdir

from pytube.exceptions import (
    VideoUnavailable,
    VideoPrivate,
    AgeRestrictedError,
    LiveStreamError,
    VideoRegionBlocked,
)
from pytube.extract import video_id


def Comprobar_Si_Se_Ha_Seleccionado_Directorio(Directorio_Descarga, log, showerror):
    """
    Comprueba si se ha seleccionado un directorio
    """

    if isdir(Directorio_Descarga.get()):
        log.writeLog("Se ha seleccionado ningún directorio para guardar el video")
        return True
    else:
        showerror(
            "Error de directorio",
            "No se ha seleccionado ningún directorio",
        )
        log.writeError("No se ha seleccionado un directorio para guardar el video")
        return False


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
    flags = DWORD()
    conexion = windll.wininet.InternetGetConnectedState(byref(flags), None)

    if conexion:
        log.writeLog("Hay conexión a internet")
        return True
    else:
        log.writeError("No hay conexión a internet")
        raise Exception("No hay conexión a internet")


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
    if VideoPrivate(__Extract_Video_ID(URL_VIDEO)):
        log.writeError("El video es privado")
        raise Exception("El video es privado")
    elif VideoUnavailable(__Extract_Video_ID(URL_VIDEO)):
        log.writeError("El video no está disponible")
        raise Exception("El video no está disponible")
    elif AgeRestrictedError(__Extract_Video_ID(URL_VIDEO)):
        log.writeError("El video está restringido por edad")
        raise Exception("El video está restringido por edad")
    elif LiveStreamError(__Extract_Video_ID(URL_VIDEO)):
        log.writeError("El video es un Live Stream")
        raise Exception("El video es un Live Stream")
    elif VideoRegionBlocked(__Extract_Video_ID(URL_VIDEO)):
        log.writeError("El video está restringido por regiones")
        raise Exception("El video está restringido por regiones")
    else:
        print("El video está disponible")
        log.writeLog("El video está disponible")
        return False


def __Extract_Video_ID(url):
    """
    Extrae el ID del video
    """
    return video_id(url)
