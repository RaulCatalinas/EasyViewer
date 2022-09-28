# Librerias necesarias
from threading import Thread
from tkinter.messagebox import showerror

# Para las constantes
from pconst import const

# Scripts necesarios
from BarraDeProgresion import BarraDeProgresion
from BarraDeTareas import BarraDeTareas
from Buscar import Buscar
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
const.ALTO_VENTANA_PRINCIPAL = 545

# -----------------------------------------------
# Ventana
ventana = Ventana(
    colorDeFondo=const.NEGRO,
    tituloVentana="Easy Viewer",
    ancho=const.ANCHO_VENTANA_PRINCIPAL,
    alto=const.ALTO_VENTANA_PRINCIPAL,
)

BarraDeTareas(ventana=ventana)

Cerrar(
    parent=ventana,
    colorFondo=const.NEGRO,
    color_Boton_Salir_Raton_Dentro=const.ROJO,
    color_Boton_Salir_Raton_Fuera=const.ROJO_OSCURO,
    color_Boton_Minimizar_Raton_Dentro=const.NARANJA,
    color_Boton_Minimizar_Raton_Fuera=const.NARANJA_OSCURO,
    color_Boton_Cancelar_Raton_Dentro=const.AMARILLO_CLARO,
    color_Boton_Cancelar_Raton_Fuera=const.AMARILLO_OSCURO,
    ancho=330,  # Ancho de la ventana de confirmación de cierre
    alto=134,  # Alto de la ventana de confirmación de cierre
    colorEtiqueta=const.AZUL_ETIQUETAS,
)

from Variables_Control import *

menu = MenuDeOpciones(ventana=ventana, textoACopiar=LINK_VIDEO)


# ------------------------------------------------

# Clase principal del programa
class Main:
    def __init__(self):
        """
        Crea la GUI para el programa.
        """
        self.buscar = Buscar(UBICACION_VIDEO=UBICACION_VIDEO)

        # Texto + Caja + Botón de descargar video
        Etiqueta(
            texto="Introduce la URL del video a descargar",
            y=10,
            ancho=30,
            colorFondo=const.AZUL_ETIQUETAS,
            fuente="Helvetica",
            tamañoFuente=18,
            ventana=ventana,
        )

        CrearEntrys(
            ventana=ventana,
            textvariable=LINK_VIDEO,
            fuente="Helvetica",
            tamañoDeFuente=15,
            ancho=70,
            y=20,
        )

        ventana.bind("<Button-3>", menu.FuncionMenuDeOpciones)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicación para guardar el video
        Etiqueta(
            texto="¿Donde quieres guardar el video?",
            y=10,
            ancho=27,
            colorFondo=const.AZUL_ETIQUETAS,
            fuente="Helvetica",
            tamañoFuente=18,
            ventana=ventana,
        )

        CrearEntrys(
            ventana=ventana,
            textvariable=UBICACION_VIDEO,
            fuente="Helvetica",
            tamañoDeFuente=15,
            ancho=70,
            y=20,
        )

        BotonPosicionAbsoluta(
            texto="Seleccionar ubicación",
            y=10,
            ancho=20,
            colorFondo=const.VERDE_OSCURO,
            funcion=lambda: [self.buscar.FuncionBuscar()],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=const.VERDE_CLARO,
            colorRatonFuera=const.VERDE_OSCURO,
        )

        BotonPosicionRelativa(
            texto="Descargar video",
            x=220,
            y=322,
            ancho=15,
            colorFondo=const.AMARILLO_OSCURO,
            funcion=lambda: [self.__Descargar_Video_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=const.AMARILLO_CLARO,
            colorRatonFuera=const.AMARILLO_OSCURO,
        )

        BotonPosicionRelativa(
            texto="Descargar audio",
            x=420,
            y=322,
            ancho=15,
            colorFondo=const.AMARILLO_OSCURO,
            funcion=lambda: [self.__Descargar_Audio_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=const.AMARILLO_CLARO,
            colorRatonFuera=const.AMARILLO_OSCURO,
        )

        # Crear la etiqueta de la barra de progresion
        Etiqueta(
            texto="Progreso de la descarga:",
            y=97,
            ancho=20,
            colorFondo=const.AZUL_ETIQUETAS,
            fuente="Helvetica",
            tamañoFuente=18,
            ventana=ventana,
        )

        self.barraDeProgresion = BarraDeProgresion(
            ventana=ventana,
            PORCENTAJE_DESCARGA=PORCENTAJE_DESCARGA,
            PORCENTAJE_DESCARGA_STRING=PORCENTAJE_DESCARGA_STRING,
            x=13,
            y=470,
        )

    def __DescargarVideo(self, URL_Video, *args, **kwargs):
        """
        Descarga el video.
        """

        print(args)
        print()
        print(kwargs)

        self.URL_Video = URL_Video

        DescargarVideo(
            LINK_VIDEO=LINK_VIDEO,
            UBICACION_VIDEO=UBICACION_VIDEO,
            PORCENTAJE_DESCARGA=PORCENTAJE_DESCARGA,
            BarraDeProgresion=self.barraDeProgresion,
            velocidad_Barra_De_Progresion=30,
        )

    def __DescargarAudio(self, URL_Video, *args, **kwargs):
        """
        Descarga el audio.
        """

        print(args)
        print()
        print(kwargs)

        self.URL_Video = URL_Video

        DescargarAudio(
            LINK_VIDEO=LINK_VIDEO,
            UBICACION_VIDEO=UBICACION_VIDEO,
            PORCENTAJE_DESCARGA=PORCENTAJE_DESCARGA,
            BarraDeProgresion=self.barraDeProgresion,
            velocidad_Barra_De_Progresion=15,
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
