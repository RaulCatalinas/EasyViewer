"""Interactua con la GUI"""
from sys import exit

from pytube import YouTube

from cliente.logging_app import GestionLogging

log = GestionLogging()


class InteractuarAPIPytube:
    """Interactua con la API de pytube"""

    def __init__(self):
        from variables_control import VariablesControl

        self.variables_control = VariablesControl()

    def get_video(self, video):
        """
        Toma un enlace a un video de YouTube y devuelve el video de mayor resolución o audio.

        :param video: booleano, devuelve el video si es true o el audio si es false
        :return: El video o audio.
        """
        _video_id = YouTube(url=self.variables_control.get_url_video())
        print(_video_id)

        if video:
            self.variables_control.set_nombre_descarga(f"{_video_id.title}.mp4")
            log.write_log("Se descargara el video")
            return _video_id.streams.get_highest_resolution()

        self.variables_control.set_nombre_descarga(f"{_video_id.title}.mp3")
        log.write_log("Se descargara el audio")
        return _video_id.streams.get_audio_only()

    @staticmethod
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
