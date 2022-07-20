from os import rename, path

from pytube import YouTube


class DescargarVideo:
    def __init__(
            self,
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            BarraDeProgresion,
            log,
            showinfo,
            showerror,
    ):
        """
        Descarga un video de YouTube y lo guarda en una carpeta que el usuario elija
        """
        self.LINK_VIDEO = LINK_VIDEO
        self.UBICACION_VIDEO = UBICACION_VIDEO
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        # Crear instancia de la barra de progresion y de la clase que gestiona el logging
        self.barra = BarraDeProgresion
        self.log = log
        self.showinfo = showinfo
        self.showerror = showerror

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

            self.showerror("Error de descarga", "No se ha conseguido descargar el video")

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeError(
                "El video no se ha podido descargar, algo ha salido mal"
            )

        else:

            self.showinfo(
                "Completado",
                "Puedes encontrar tu video en:\n" + self.Carpeta_Guardar_Video,
            )

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
            showinfo,
            showerror,
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
        self.showinfo = showinfo
        self.showerror = showerror

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

            self.showerror("Error de descarga", "No se ha conseguido descargar el audio")

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeError(
                "El audio no se ha podido descargar, algo ha salido mal"
            )

        else:
            self.cambiarFormato = self.base + ".mp3"

            rename(self.base + self.ext, self.cambiarFormato)

            self.showinfo(
                "Completado",
                "Puedes encontrar el audio del video en:\n"
                + self.Carpeta_Guardar_Video,
            )

            self.barra.barraProgresionDescarga["value"] = 0

            self.PORCENTAJE_DESCARGA.set("")

            self.log.writeLog(
                "La variable que guarda el porcentaje de la descarga de se "
                "ha restablecido correctamente"
            )

            self.log.writeLog(
                "La descarga del audio del video se ha completado correctamente"
            )
