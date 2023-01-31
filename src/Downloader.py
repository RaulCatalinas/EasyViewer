from webbrowser import open

import interactuar_gui as gui
from logging_app import GestionLogging as log


class Descargar:
    """
    Descarga un video o el audio de un video de YouTube y lo guarda en una ubicación específica
    """

    def __init__(
        self,
        barra_de_progresion,
        boton_seleccionar_ubicacion,
        boton_descargar_video,
        boton_descargar_audio,
        entry_url,
        entry_ubicacion_video,
        descargar_video,
    ):
        self.barra_de_progresion = barra_de_progresion
        self.boton_seleccionar_ubicacion = boton_seleccionar_ubicacion
        self.boton_descargar_video = boton_descargar_video
        self.boton_descargar_audio = boton_descargar_audio
        self.boton_descargar_video = boton_descargar_video
        self.entry_url = entry_url
        self.entry_ubicacion_video = entry_ubicacion_video
        self.descargar_video = descargar_video

        try:
            self.__desactivar_widgets()

            if self.descargar_video:
                self.descargar = gui.get_video(True)
            else:
                self.descargar = gui.get_video(False)

            self.barra_de_progresion.ejecutar_barra_de_progresion()

            self.descargar.download(
                output_path=gui.get_ubicacion_video(),
                filename=gui.get_nombre_descarga(),
            )

        except Exception as exc:
            self.barra_de_progresion.detener_barra_de_progresion()

            self.__activar_widgets()

            log.write_error(str(exc))

            raise Exception(str(exc)) from exc

        else:
            open(gui.get_ubicacion_video())

            self.barra_de_progresion.detener_barra_de_progresion()

            self.__activar_widgets()

            log.write_log("Descarga completada correctamente")

    def __desactivar_widgets(self):
        self.boton_seleccionar_ubicacion.desactivar()
        self.boton_descargar_video.desactivar()
        self.boton_descargar_audio.desactivar()
        self.entry_url.desactivar()
        self.entry_ubicacion_video.desactivar()

    def __activar_widgets(self):
        self.boton_seleccionar_ubicacion.activar()
        self.boton_descargar_video.activar()
        self.boton_descargar_audio.activar()
        self.entry_url.activar()
        self.entry_ubicacion_video.activar()
