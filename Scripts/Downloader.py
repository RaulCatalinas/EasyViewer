from os import rename, path
from webbrowser import open

from pytube import YouTube


class DescargarVideo:
    def __init__(
            self,
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            BarraDeProgresion,
            log,
    ):
        """
        Descarga un video de YouTube y lo guarda en una carpeta que el usuario elija
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.barra = BarraDeProgresion
        self.log = log

        self.log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.URL = self.LINK_VIDEO.get()

            self.log.writeLog("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = self.UBICACION_VIDEO.get()

            self.log.writeLog(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = YouTube(self.URL)

            self.log.writeLog("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_highest_resolution()

            self.log.writeLog(
                "Se ha obtenido la resolución mas alta del video a descargar"
            )

            self.Descargar_Video.download(self.Carpeta_Guardar_Video)

        except:

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeError(
                "El video no se ha podido descargar, algo ha salido mal"
            )

            raise Exception("El video no se ha podido descargar")

        else:

            open(self.Carpeta_Guardar_Video)

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeLog("La descarga del video se ha completado correctamente")


class DescargarAudio:
    def __init__(
            self,
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            BarraDeProgresion,
            log,
    ):
        """
        Descarga el audio de un vídeo de YouTube y lo guarda en la carpeta que el usuario haya elegido
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        # Crear instancia de la barra de progresion
        self.barra = BarraDeProgresion
        self.log = log

        self.log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.URL = self.LINK_VIDEO.get()

            self.log.writeLog("Se ha obtenido la URL del video a descargar")

            self.Carpeta_Guardar_Video = self.UBICACION_VIDEO.get()

            self.log.writeLog(
                "Se ha obtenido la dirección de la carpeta donde se quiere guardar el video descargado"
            )

            self.Obtener_Video = YouTube(self.URL)

            self.log.writeLog("Se ha obtenido el ID del video a descargar")

            self.Descargar_Video = self.Obtener_Video.streams.get_audio_only()

            self.log.writeLog("Se ha obtenido el audio del video a descargar")

            self.base, self.ext = path.splitext(
                self.Descargar_Video.download(self.Carpeta_Guardar_Video)
            )

        except:

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeError(
                "El audio no se ha podido descargar, algo ha salido mal"
            )

            raise Exception("El audio no se ha podido descargar")

        else:
            self.cambiarFormato = self.base + ".mp3"

            rename(self.base + self.ext, self.cambiarFormato)

            open(self.Carpeta_Guardar_Video)

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeLog(
                "La descarga del audio del video se ha completado correctamente"
            )
