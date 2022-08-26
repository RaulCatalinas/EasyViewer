# Librerias necesarias
from threading import Thread
from tkinter.messagebox import showerror

# Para las constantes
from pconst import const

# Scripts necesarios
from BarraDeProgresion import BarraDeProgresion
from Buscar import Buscar
from CentrarVentana import CentrarVentana
from Cerrar import Cerrar
from CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from CrearEntrys import CrearEntrys
from CrearEtiquetas import Etiqueta
from Downloader import *
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
const.ROJO = "#FF0000"
const.ROJO_OSCURO = "#660000"
const.NARANJA = "#FF8000"
const.NARANJA_OSCURO = "#663300"
const.ANCHO_VENTANA_PRINCIPAL = 830
const.ALTO_VENTANA_PRINCIPAL = 520

# -----------------------------------------------
# Ventana
ventana = Ventana(
    const.NEGRO,
    "Easy Viewer",
    const.ANCHO_VENTANA_PRINCIPAL,
    const.ALTO_VENTANA_PRINCIPAL,
)

CentrarVentana(ventana, const.ANCHO_VENTANA_PRINCIPAL, const.ALTO_VENTANA_PRINCIPAL)

Cerrar(
    ventana,
    const.NEGRO,
    const.ROJO,
    const.ROJO_OSCURO,
    const.NARANJA,
    const.NARANJA_OSCURO,
    const.AMARILLO_CLARO,
    const.AMARILLO_OSCURO,
    330,  # Ancho de la ventana de confirmación de cierre
    134,  # Alto de la ventana de confirmación de cierre
    const.AZUL_ETIQUETAS,
)

from Variables_Control import *

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
        self.buscar = Buscar(UBICACION_VIDEO)

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
            lambda: [self.__Descargar_Video_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
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
            lambda: [self.__Descargar_Audio_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
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

    def __DescargarVideo(self, URL_Video):
        """
        Descarga el video.
        """
        self.URL_Video = URL_Video

        self.barraDeProgresion.GB = ObtenerTamañoVideo(self.URL_Video)

        DescargarVideo(
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            self.barraDeProgresion,
            30,
        )

    def __DescargarAudio(self, URL_Video):
        """
        Descarga el audio.
        """
        self.URL_Video = URL_Video

        self.barraDeProgresion.GB = ObtenerTamañoAudio(self.URL_Video)

        DescargarAudio(
            LINK_VIDEO,
            UBICACION_VIDEO,
            PORCENTAJE_DESCARGA,
            self.barraDeProgresion,
            15,
        )

    def __Descargar_Video_En_Un_Hilo_Nuevo(self, URL_Video):
        self.URL_Video = URL_Video
        try:
            if (
                Comprobar_Si_Se_Ha_Introducido_Una_URL(
                    self.URL_Video,
                )
                and Comprobar_Si_Es_URL_YouTube(
                    self.URL_Video,
                )
                and Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                )
                and Comprobar_Conexion_Internet()
                and Comprobar_Si_El_Video_Esta_Disponible(self.URL_Video)
            ):
                Thread(target=self.barraDeProgresion.AumentarProgreso()).start()
                Thread(target=self.__DescargarVideo, args=self.URL_Video).start()
        except Exception as e:
            showerror("Error", str(e))

    def __Descargar_Audio_En_Un_Hilo_Nuevo(self, URL_Video):
        self.URL_Video = URL_Video
        try:
            if (
                Comprobar_Si_Se_Ha_Introducido_Una_URL(
                    self.URL_Video,
                )
                and Comprobar_Si_Es_URL_YouTube(
                    self.URL_Video,
                )
                and Comprobar_Si_Se_Ha_Seleccionado_Directorio(
                    UBICACION_VIDEO,
                )
                and Comprobar_Conexion_Internet()
                and Comprobar_Si_El_Video_Esta_Disponible(self.URL_Video)
            ):
                Thread(target=self.barraDeProgresion.AumentarProgreso()).start()
                Thread(target=self.__DescargarAudio, args=self.URL_Video).start()
        except Exception as e:
            showerror("Error", str(e))


Main()
# Actualizar ventana
ventana.ActualizarVentana()
