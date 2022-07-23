from tkinter.messagebox import showinfo, showerror

from Scripts.Aumentar_Barra_De_Progresion_En_Paralelo import (
    AumentarBarraDeProgresionEnParalelo,
)
from Scripts.BarraDeProgresion import BarraDeProgresion
from Scripts.Buscar import Buscar
from Scripts.Constantes import Colores
from Scripts.CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from Scripts.CrearEntrys import CrearEntrys
from Scripts.CrearEtiquetas import Etiqueta
from Scripts.Downloader import DescargarVideo, DescargarAudio
from Scripts.Logging import GestionLogging as log
from Scripts.Menu_De_Opciones import MenuDeOpciones
from Scripts.Validaciones import (
    Comprobar_Si_Se_Ha_Seleccionado_Directorio,
    Comprobar_Si_Es_URL_YouTube,
    Comprobar_Conexion_Internet,
    Comprobar_Si_Se_Ha_Introducido_Una_URL,
)
from Scripts.Ventana import Ventana

# -----------------------------------------------
# Ventana
ventana = Ventana(Colores.NEGRO.value)
menu = MenuDeOpciones(ventana)

from Scripts.Variables_Control import (
    UBICACION_VIDEO,
    LINK_VIDEO,
    PORCENTAJE_DESCARGA,
    PORCENTAJE_DESCARGA_STRING,
)


# ------------------------------------------------

# Clase principal del programa
class Main:
    def __init__(self):
        """
        Crea la GUI para el programa.
        """
        self.barraDeProgresion = BarraDeProgresion(
            ventana,
            PORCENTAJE_DESCARGA,
            PORCENTAJE_DESCARGA_STRING,
            13,
            470,
        )
        self.buscar = Buscar(UBICACION_VIDEO, log, showerror)
        self.aumentarBarraDeProgreso = AumentarBarraDeProgresionEnParalelo(
            PORCENTAJE_DESCARGA,
            log,
            self.barraDeProgresion,
        )

        # Texto + Caja + Botón de descargar video
        self.Etiqueta_URL = Etiqueta(
            "Introduce la URL del video a descargar",
            10,
            30,
            Colores.AZUL_ETIQUETAS.value,
            "Helvetica",
            18,
            ventana,
        )

        self.URL_Video = CrearEntrys(ventana, LINK_VIDEO, "Helvetica", 15, 70, 20)

        ventana.bind("<Button-3>", menu.FuncionMenuDeOpciones)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicación para guardar el video
        self.Ubicacion = Etiqueta(
            "¿Donde quieres guardar el video?",
            10,
            27,
            Colores.AZUL_ETIQUETAS.value,
            "Helvetica",
            18,
            ventana,
        )

        self.Ubicacion_Video = CrearEntrys(
            ventana, UBICACION_VIDEO, "Helvetica", 15, 70, 20
        )

        self.Boton_Buscar = BotonPosicionAbsoluta(
            "Seleccionar ubicación",
            10,
            20,
            Colores.VERDE_OSCURO.value,
            lambda: [self.buscar.FuncionBuscar()],
            "Helvetica",
            15,
            ventana,
            Colores.VERDE_CLARO.value,
            Colores.VERDE_OSCURO.value,
        )

        self.Boton_Descargar_Video = BotonPosicionRelativa(
            "Descargar video",
            220,
            322,
            15,
            Colores.AMARILLO_OSCURO.value,
            lambda: [self.__DescargarVideo(
                LINK_VIDEO.get(),
                Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                    log,
                    showerror,
                ),
                log
            )],
            "Helvetica",
            15,
            ventana,
            Colores.AMARILLO_CLARO.value,
            Colores.AMARILLO_OSCURO.value,
        )

        self.Boton_Descargar_Audio = BotonPosicionRelativa(
            "Descargar audio",
            420,
            322,
            15,
            Colores.AMARILLO_OSCURO.value,
            lambda: [self.__DescargarAudio(
                LINK_VIDEO.get(),
                Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                    log,
                    showerror,
                ),
                log
            )],
            "Helvetica",
            15,
            ventana,
            Colores.AMARILLO_CLARO.value,
            Colores.AMARILLO_OSCURO.value,
        )

        # Crear la etiqueta de la barra de progresion
        self.Etiqueta_Barra_Progress = Etiqueta(
            "Progreso de la descarga:",
            97,
            20,
            Colores.AZUL_ETIQUETAS.value,
            "Helvetica",
            18,
            ventana,
        )

    def __DescargarVideo(self, URL_Video, comprobarDirectorio, log):
        """
        Descarga el video.
        """
        self.URL_Video = URL_Video
        self.comprobarDirectorio = comprobarDirectorio
        self.log = log

        try:
            if (
                    Comprobar_Si_Se_Ha_Introducido_Una_URL(
                        self.URL_Video,
                        self.log,
                    )
                    and self.comprobarDirectorio
                    and Comprobar_Conexion_Internet(self.log)
                    and Comprobar_Si_Es_URL_YouTube(
                self.URL_Video,
                self.log,
            )
            ):
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo()
                DescargarVideo(
                    LINK_VIDEO,
                    UBICACION_VIDEO,
                    PORCENTAJE_DESCARGA,
                    self.barraDeProgresion,
                    log,
                    showinfo,
                )

        except Exception as e:
            showerror("Error", str(e))

    def __DescargarAudio(self, URL_Video, comprobarDirectorio, log):
        """
        Descarga el audio.
        """
        self.URL_Video = URL_Video
        self.comprobarDirectorio = comprobarDirectorio
        self.log = log

        try:
            if (
                    Comprobar_Si_Se_Ha_Introducido_Una_URL(
                        self.URL_Video,
                        self.log,
                    )
                    and self.comprobarDirectorio
                    and Comprobar_Conexion_Internet(self.log)
                    and Comprobar_Si_Es_URL_YouTube(
                self.URL_Video,
                self.log,
            )
            ):
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo()
                DescargarAudio(
                    LINK_VIDEO,
                    UBICACION_VIDEO,
                    PORCENTAJE_DESCARGA,
                    self.barraDeProgresion,
                    log,
                    showinfo,
                )
        except Exception as e:
            showerror("Error", str(e))


Main()
# Actualizar ventana
ventana.ActualizarVentana()
