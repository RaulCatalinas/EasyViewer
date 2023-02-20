"""Interactua con la GUI"""
from sys import exit

from pytube import YouTube

from logging_app import GestionLogging

log = GestionLogging()


def get_video(video):
    """
    Toma un enlace a un video de YouTube y devuelve el video de mayor resolución o audio.

    :param video: booleano, devuelve el video si es true o el audio si es false
    :return: El video o audio.
    """
    from variables_control import LINK_VIDEO, NOMBRE_DESCARGA

    _video_id = YouTube(LINK_VIDEO.get())
    if video:
        NOMBRE_DESCARGA.set(f"{_video_id.title}.mp4")
        log.write_log("Se descargara el video")
        return _video_id.streams.get_highest_resolution()

    NOMBRE_DESCARGA.set(f"{_video_id.title}.mp3")
    log.write_log("Se descargara el audio")
    return _video_id.streams.get_audio_only()


def get_ubicacion_video():
    """
    Devuelve la ubicacion seleccionada por el usuario
    :return: La ubicacion seleccionada por el usuario
    """
    from variables_control import UBICACION_VIDEO

    return UBICACION_VIDEO.get()


def get_nombre_descarga():
    """
    Devuelve el nombre de la descarga
    :return: El nombre de la descarga
    """
    from variables_control import NOMBRE_DESCARGA

    return NOMBRE_DESCARGA.get()


def set_descargado_correctamente(descargado):
    from variables_control import DESCARGADO_CORRECTAMENTE

    return DESCARGADO_CORRECTAMENTE.set(descargado)


def get_descargado_correctamente():
    from variables_control import DESCARGADO_CORRECTAMENTE

    return DESCARGADO_CORRECTAMENTE.get()


def cancelar_descarga():
    """
    Cancela la descarga del video y/o audio y despues lo elimina
    """
    try:
        raise KeyboardInterrupt("Descarga cancelada por el usuario")
    except KeyboardInterrupt as exc:
        print(exc)
        print()
        log.write_error(str(exc))
    finally:
        exit()
