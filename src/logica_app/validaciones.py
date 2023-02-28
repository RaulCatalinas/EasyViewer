"""Comprobaciones ha realizar antes de descargar el video y/o el audio"""

from os import environ
from os.path import isdir, join

import requests
from pytube import YouTube

from cliente.get_config import Config
from cliente.logging_app import GestionLogging

log = GestionLogging()
config = Config()


def comprobar_si_se_ha_seleccionado_directorio(directorio_descarga):
    """
    Comprueba si se ha seleccionado un directorio
    """

    if directorio_descarga.get() != "" and isdir(directorio_descarga.get()):
        log.write_log("Se ha seleccionado un directorio para guardar el video")
        return True

    log.write_error("Se ha establecido el directorio por defecto")
    directorio_descarga.set(join(join(environ["USERPROFILE"]), "Desktop"))
    return True


def comprobar_si_es_url_youtube(url):
    """
    Comprueba si la URL es de YouTube
    """
    if (
        "https://www.youtube.com/watch?v=" in url.get()
        or "https://youtu.be/" in url.get()
        or "https://www.youtube.com/shorts/" in url.get()
    ):
        log.write_log("La URL es de YouTube")
        return True

    log.write_error("La URL no es de YouTube")
    raise Exception(config.get_config_execel(17))


def comprobar_conexion_internet():
    """
    Comprueba si hay conexión a internet
    """
    try:
        requests.get("https://www.google.es", timeout=5)
    except (requests.ConnectionError, requests.Timeout) as exc:
        log.write_error("No hay conexión a internet")
        raise Exception(config.get_config_execel(16)) from exc

    log.write_log("Si hay conexión a internet")
    return True


def comprobar_si_se_ha_introducido_una_url(url):
    """
    Comprueba si se ha introducido una URL
    """
    if url.get() == "":
        log.write_error("No se ha introducido ninguna URL")
        raise Exception(config.get_config_execel(15))

    log.write_log("Se ha introducido una URL")
    return True


def comprobar_si_el_video_esta_disponible(url):
    """
    Comprueba si el video está disponible
    """
    try:
        YouTube(url.get()).check_availability()
        log.write_log("El video esta disponible")
        return True

    except Exception as exc:
        log.write_error(str(exc))
        raise Exception(str(exc)) from exc
