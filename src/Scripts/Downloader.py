from os import rename
from os.path import splitext
from webbrowser import open

from pytube import YouTube

from Logging import GestionLogging

log = GestionLogging()


class DescargarVideo:
    def __init__(
        self,
        LINK_VIDEO,
        UBICACION_VIDEO,
        PORCENTAJE_DESCARGA,
        BarraDeProgresion,
        velocidad_Barra_De_Progresion,
    ):
        """
        Descarga un video de YouTube y lo guarda en una carpeta que el usuario elija
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.barra = BarraDeProgresion
        self.velocidad_Barra_De_Progresion = velocidad_Barra_De_Progresion

        log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.URL = self.LINK_VIDEO.get()

            log.writeLog("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = self.UBICACION_VIDEO.get()

            log.writeLog(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = YouTube(self.URL)

            log.writeLog("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_highest_resolution()

            log.writeLog("Se ha obtenido la resolución mas alta del video a descargar")

            self.__EjecutarBarraDeProgresion(self.velocidad_Barra_De_Progresion)

            self.Descargar_Video.download(self.Carpeta_Guardar_Video)

        except:
            self.__DetenerBarraDeProgresion()

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.writeError("El video no se ha podido descargar, algo ha salido mal")

            raise Exception("El video no se ha podido descargar")

        else:
            open(self.Carpeta_Guardar_Video)

            self.__DetenerBarraDeProgresion()

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.writeLog("La descarga del video se ha completado correctamente")

    def __EjecutarBarraDeProgresion(self, velocidad):
        self.barra.barraProgresionDescarga.start(velocidad)

    def __DetenerBarraDeProgresion(self):
        self.barra.barraProgresionDescarga.stop()


class DescargarAudio:
    def __init__(
        self,
        LINK_VIDEO,
        UBICACION_VIDEO,
        PORCENTAJE_DESCARGA,
        BarraDeProgresion,
        velocidad_Barra_De_Progresion,
    ):
        """
        Descarga el audio de un vídeo de YouTube y lo guarda en la carpeta que el usuario haya elegido
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.barra = BarraDeProgresion
        self.velocidad_Barra_De_Progresion = velocidad_Barra_De_Progresion

        log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.URL = self.LINK_VIDEO.get()

            log.writeLog("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = self.UBICACION_VIDEO.get()

            log.writeLog(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = YouTube(self.URL)

            log.writeLog("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_audio_only()

            log.writeLog("Se ha obtenido el audio del video a descargar")

            self.__EjecutarBarraDeProgresion(self.velocidad_Barra_De_Progresion)

            self.base, self.ext = splitext(
                self.Descargar_Video.download(self.Carpeta_Guardar_Video)
            )

        except:
            self.__DetenerBarraDeProgresion()

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.writeError("El audio no se ha podido descargar, algo ha salido mal")

            raise Exception("El audio no se ha podido descargar")

        else:
            self.cambiarFormato = self.base + ".mp3"

            rename(self.base + self.ext, self.cambiarFormato)

            open(self.Carpeta_Guardar_Video)

            self.__DetenerBarraDeProgresion()

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.writeLog(
                "La descarga del audio del video se ha completado correctamente"
            )

    def __EjecutarBarraDeProgresion(self, velocidad):
        self.barra.barraProgresionDescarga.start(velocidad)

    def __DetenerBarraDeProgresion(self):
        self.barra.barraProgresionDescarga.stop()
