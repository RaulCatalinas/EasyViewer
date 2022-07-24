from ctypes import windll, byref
from ctypes.wintypes import DWORD
from os.path import isdir


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
