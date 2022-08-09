# modulos necesarios
from os.path import abspath
from threading import Thread
from tkinter.messagebox import showerror

# Para las constantes
from pconst import const

# Scripts necesarios
from BarraDeProgresion import BarraDeProgresion
from Buscar import Buscar
from CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from CrearEntrys import CrearEntrys
from CrearEtiquetas import Etiqueta
from Downloader import *
from Logging import GestionLogging as log
from Menu_De_Opciones import MenuDeOpciones
from Validaciones import *
from Ventana import Ventana

# -------------------------------------------------
# Constantes

const.AZUL_ETIQUETAS = "#00FFEF"
const.VERDE_OSCURO = "#003300"
const.VERDE_CLARO = "#00FF00"
const.NEGRO = "#000000"
const.AMARILLO_OSCURO = "#333300"
const.AMARILLO_CLARO = "#FFFF00"
const.RUTA_ABSOLUTA = abspath("../Icon/Icono.ico")

# -----------------------------------------------
# Ventana
ventana = Ventana(const.NEGRO, const.RUTA_ABSOLUTA)

from Scripts.Variables_Control import *

menu = MenuDeOpciones(ventana, LINK_VIDEO)


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

        # Texto + Caja + Botón de descargar video
        Etiqueta(
            "Introduce la URL del video a descargar",
            10,
            30,
            const.AZUL_ETIQUETAS,
            "Helvetica",
            18,
            ventana,
        )

        CrearEntrys(ventana, LINK_VIDEO, "Helvetica", 15, 70, 20)

        ventana.bind("<Button-3>", menu.FuncionMenuDeOpciones)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicación para guardar el video
        Etiqueta(
            "¿Donde quieres guardar el video?",
            10,
            27,
            const.AZUL_ETIQUETAS,
            "Helvetica",
            18,
            ventana,
        )

        CrearEntrys(ventana, UBICACION_VIDEO, "Helvetica", 15, 70, 20)

        BotonPosicionAbsoluta(
            "Seleccionar ubicación",
            10,
            20,
            const.VERDE_OSCURO,
            lambda: [self.buscar.FuncionBuscar()],
            "Helvetica",
            15,
            ventana,
            const.VERDE_CLARO,
            const.VERDE_OSCURO,
        )

        BotonPosicionRelativa(
            "Descargar video",
            220,
            322,
            15,
            const.AMARILLO_OSCURO,
            lambda: [self.__Descargar_Video_En_Un_Hilo_Nuevo(LINK_VIDEO.get(), log)],
            "Helvetica",
            15,
            ventana,
            const.AMARILLO_CLARO,
            const.AMARILLO_OSCURO,
        )

        BotonPosicionRelativa(
            "Descargar audio",
            420,
            322,
            15,
            const.AMARILLO_OSCURO,
            lambda: [self.__Descargar_Audio_En_Un_Hilo_Nuevo(LINK_VIDEO.get(), log)],
            "Helvetica",
            15,
            ventana,
            const.AMARILLO_CLARO,
            const.AMARILLO_OSCURO,
        )

        # Crear la etiqueta de la barra de progresion
        Etiqueta(
            "Progreso de la descarga:",
            97,
            20,
            const.AZUL_ETIQUETAS,
            "Helvetica",
            18,
            ventana,
        )

    def __DescargarVideo(self, URL_Video, log):
        """
        Descarga el video.
        """
        self.URL_Video = URL_Video
        self.log = log

        self.barraDeProgresion.GB = ObtenerTamañoVideo(self.URL_Video, log)

        DescargarVideo(
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            self.barraDeProgresion,
            log,
            30,
        )

    def __DescargarAudio(self, URL_Video, log):
        """
        Descarga el audio.
        """
        self.URL_Video = URL_Video
        self.log = log

        self.barraDeProgresion.GB = ObtenerTamañoAudio(self.URL_Video, log)

        DescargarAudio(
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            self.barraDeProgresion,
            log,
            15,
        )

    def __Descargar_Video_En_Un_Hilo_Nuevo(self, URL_Video, log):
        self.URL_Video = URL_Video
        self.log = log
        try:
            if (
                Comprobar_Si_Se_Ha_Introducido_Una_URL(
                    self.URL_Video,
                    self.log,
                )
                and Comprobar_Si_Es_URL_YouTube(
                    self.URL_Video,
                    self.log,
                )
                and Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                    self.log,
                )
                and Comprobar_Conexion_Internet(self.log)
                and Comprobar_Si_El_Video_Esta_Disponible(self.log, self.URL_Video)
            ):
                Thread(target=self.barraDeProgresion.AumentarProgreso()).start()
                Thread(
                    target=self.__DescargarVideo, args=(self.URL_Video, self.log)
                ).start()
        except Exception as e:
            showerror("Error", str(e))

    def __Descargar_Audio_En_Un_Hilo_Nuevo(self, URL_Video, log):
        self.URL_Video = URL_Video
        self.log = log
        try:
            if (
                Comprobar_Si_Se_Ha_Introducido_Una_URL(
                    self.URL_Video,
                    self.log,
                )
                and Comprobar_Si_Es_URL_YouTube(
                    self.URL_Video,
                    self.log,
                )
                and Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                    self.log,
                )
                and Comprobar_Conexion_Internet(self.log)
                and Comprobar_Si_El_Video_Esta_Disponible(self.log, self.URL_Video)
            ):
                Thread(target=self.barraDeProgresion.AumentarProgreso()).start()
                Thread(
                    target=self.__DescargarAudio, args=(self.URL_Video, self.log)
                ).start()
        except Exception as e:
            showerror("Error", str(e))


Main()
# Actualizar ventana
ventana.ActualizarVentana()
