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
        boton_Seleccionar_Ubicacion,
        boton_Descargar_Video,
        boton_Descargar_Audio,
        entry_URL,
        entry_Ubicacion_Video,
        NOMBRE_DESCARGA,
    ):
        """
        Descarga un video de YouTube y lo guarda en una carpeta que el usuario elija
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.barra = BarraDeProgresion
        self.velocidad_Barra_De_Progresion = velocidad_Barra_De_Progresion
        self.boton_Descargar_Audio = boton_Descargar_Audio
        self.boton_Descargar_Video = boton_Descargar_Video
        self.boton_Seleccionar_Ubicacion = boton_Seleccionar_Ubicacion
        self.entry_Ubicacion_Video = entry_Ubicacion_Video
        self.entry_URL = entry_URL
        self.NOMBRE_DESCARGA = NOMBRE_DESCARGA

        log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.boton_Seleccionar_Ubicacion.DesactivarBoton()
            self.boton_Descargar_Video.DesactivarBoton()
            self.boton_Descargar_Audio.DesactivarBoton()
            self.entry_URL.DesactivarEntry()
            self.entry_Ubicacion_Video.DesactivarEntry()

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

            self.espaciosEliminados = self.Obtener_Video.title.replace(" ", "-")
            self.comasEliminadas = self.espaciosEliminados.replace(",", "")
            self.exclamacionDeAperturaEliminada = self.comasEliminadas.replace("¡", "")
            self.exclamacionDeCierreEliminada = (
                self.exclamacionDeAperturaEliminada.replace("!", "")
            )

            print(self.exclamacionDeCierreEliminada)

            self.NOMBRE_DESCARGA.set(f"{self.exclamacionDeCierreEliminada}.mp4")

            self.Descargar_Video.download(
                self.Carpeta_Guardar_Video, filename=self.NOMBRE_DESCARGA.get()
            )

        except:
            self.__DetenerBarraDeProgresion()

            self.boton_Seleccionar_Ubicacion.ActivarBoton()
            self.boton_Descargar_Video.ActivarBoton()
            self.boton_Descargar_Audio.ActivarBoton()
            self.entry_URL.ActivarEntry()
            self.entry_Ubicacion_Video.ActivarEntry()

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

            self.boton_Seleccionar_Ubicacion.ActivarBoton()
            self.boton_Descargar_Video.ActivarBoton()
            self.boton_Descargar_Audio.ActivarBoton()
            self.entry_URL.ActivarEntry()
            self.entry_Ubicacion_Video.ActivarEntry()

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
        boton_Seleccionar_Ubicacion,
        boton_Descargar_Video,
        boton_Descargar_Audio,
        entry_URL,
        entry_Ubicacion_Video,
        NOMBRE_DESCARGA,
    ):
        """
        Descarga el audio de un vídeo de YouTube y lo guarda en la carpeta que el usuario haya elegido
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.barra = BarraDeProgresion
        self.velocidad_Barra_De_Progresion = velocidad_Barra_De_Progresion
        self.boton_Descargar_Audio = boton_Descargar_Audio
        self.boton_Descargar_Video = boton_Descargar_Video
        self.boton_Seleccionar_Ubicacion = boton_Seleccionar_Ubicacion
        self.entry_Ubicacion_Video = entry_Ubicacion_Video
        self.entry_URL = entry_URL
        self.NOMBRE_DESCARGA = NOMBRE_DESCARGA

        log.writeLog("Se ha hecho click en el botón de descargar")

        try:
            self.boton_Seleccionar_Ubicacion.DesactivarBoton()
            self.boton_Descargar_Video.DesactivarBoton()
            self.boton_Descargar_Audio.DesactivarBoton()
            self.entry_URL.DesactivarEntry()
            self.entry_Ubicacion_Video.DesactivarEntry()

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

            self.espaciosEliminados = self.Obtener_Video.title.replace(" ", "-")
            self.comasEliminadas = self.espaciosEliminados.replace(",", "")
            self.exclamacionDeAperturaEliminada = self.comasEliminadas.replace("¡", "")
            self.exclamacionDeCierreEliminada = (
                self.exclamacionDeAperturaEliminada.replace("!", "")
            )

            print(self.exclamacionDeCierreEliminada)

            self.NOMBRE_DESCARGA.set(f"{self.exclamacionDeCierreEliminada}.mp3")

            self.Descargar_Video.download(
                self.Carpeta_Guardar_Video,
                filename=self.NOMBRE_DESCARGA.get(),
            )

        except:
            self.__DetenerBarraDeProgresion()

            self.boton_Seleccionar_Ubicacion.ActivarBoton()
            self.boton_Descargar_Video.ActivarBoton()
            self.boton_Descargar_Audio.ActivarBoton()
            self.entry_URL.ActivarEntry()
            self.entry_Ubicacion_Video.ActivarEntry()

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            log.writeError("El audio no se ha podido descargar, algo ha salido mal")

            raise Exception("El audio no se ha podido descargar")

        else:
            open(self.Carpeta_Guardar_Video)

            self.boton_Seleccionar_Ubicacion.ActivarBoton()
            self.boton_Descargar_Video.ActivarBoton()
            self.boton_Descargar_Audio.ActivarBoton()
            self.entry_URL.ActivarEntry()
            self.entry_Ubicacion_Video.ActivarEntry()

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
