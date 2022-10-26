# Librerias necesarias
from configparser import ConfigParser
from threading import Thread
from tkinter.messagebox import showerror

# Scripts necesarios
from BarraDeProgresion import BarraDeProgresion
from BarraDeTareas import BarraDeTareas
from Buscar import Buscar
from Cerrar import Cerrar
from Config.Ruta_Del_Archivo_De_Configuracion import *
from CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from CrearEntrys import CrearEntrys
from CrearEtiquetas import Etiqueta
from Downloader import *
from Menu_De_Opciones import MenuDeOpciones
from Validaciones import *
from Ventana import Ventana

config = ConfigParser()

hiloDescargarVideo = None
hiloProgresionVideo = None
hiloDescargarAudio = None
hiloProgresionAudio = None

config.read(Ruta_Del_Archivo_De_Configuracion())
chdir(dirname(__file__))

# Ventana
ventana = Ventana(
    colorDeFondo=config["COLORES"]["NEGRO"],
    tituloVentana=config["VENTANA"]["TITULO"],
    ancho=config.getint("VENTANA", "ANCHO"),
    alto=config.getint("VENTANA", "ALTO"),
)

BarraDeTareas(ventana=ventana)


Cerrar(
    parent=ventana,
    colorFondo=config["COLORES"]["NEGRO"],
    color_Boton_Salir_Raton_Dentro=config["COLORES"]["ROJO"],
    color_Boton_Salir_Raton_Fuera=config["COLORES"]["ROJO_OSCURO"],
    color_Boton_Minimizar_Raton_Dentro=config["COLORES"]["NARANJA"],
    color_Boton_Minimizar_Raton_Fuera=config["COLORES"]["NARANJA_OSCURO"],
    color_Boton_Cancelar_Raton_Dentro=config["COLORES"]["AMARILLO"],
    color_Boton_Cancelar_Raton_Fuera=config["COLORES"]["AMARILLO_OSCURO"],
    ancho=config.getint("VENTANA_CONTROL_CIERRE", "ANCHO"),
    alto=config.getint("VENTANA_CONTROL_CIERRE", "ALTO"),
    colorEtiqueta=config["COLORES"]["AZUL_ETIQUETAS"],
    tituloVentana=config["VENTANA_CONTROL_CIERRE"]["TITULO"],
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
            colorFondo=config["COLORES"]["AZUL_ETIQUETAS"],
            fuente="Helvetica",
            tamañoFuente=18,
            ventana=ventana,
        )

        self.entry_URL = CrearEntrys(
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
            colorFondo=config["COLORES"]["AZUL_ETIQUETAS"],
            fuente="Helvetica",
            tamañoFuente=18,
            ventana=ventana,
        )

        self.entry_Ubicacion_Video = CrearEntrys(
            ventana=ventana,
            textvariable=UBICACION_VIDEO,
            fuente="Helvetica",
            tamañoDeFuente=15,
            ancho=70,
            y=20,
        )

        self.boton_Seleccionar_Ubicacion = BotonPosicionAbsoluta(
            texto="Seleccionar ubicación",
            y=10,
            ancho=20,
            colorFondo=config["COLORES"]["VERDE_OSCURO"],
            funcion=lambda: [self.buscar.FuncionBuscar()],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=config["COLORES"]["VERDE"],
            colorRatonFuera=config["COLORES"]["VERDE_OSCURO"],
        )

        self.boton_Descargar_Video = BotonPosicionRelativa(
            texto="Descargar video",
            x=220,
            y=322,
            ancho=15,
            colorFondo=config["COLORES"]["AMARILLO_OSCURO"],
            funcion=lambda: [self.__Descargar_Video_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=config["COLORES"]["AMARILLO"],
            colorRatonFuera=config["COLORES"]["AMARILLO_OSCURO"],
        )

        self.boton_Descargar_Audio = BotonPosicionRelativa(
            texto="Descargar audio",
            x=420,
            y=322,
            ancho=15,
            colorFondo=config["COLORES"]["AMARILLO_OSCURO"],
            funcion=lambda: [self.__Descargar_Audio_En_Un_Hilo_Nuevo(LINK_VIDEO.get())],
            fuente="Helvetica",
            tamañoFuente=15,
            ventana=ventana,
            colorRatonDentro=config["COLORES"]["AMARILLO"],
            colorRatonFuera=config["COLORES"]["AMARILLO_OSCURO"],
        )

        # Crear la etiqueta de la barra de progresion
        Etiqueta(
            texto="Progreso de la descarga:",
            y=97,
            ancho=20,
            colorFondo=config["COLORES"]["AZUL_ETIQUETAS"],
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
            boton_Descargar_Video=self.boton_Descargar_Video,
            boton_Descargar_Audio=self.boton_Descargar_Audio,
            boton_Seleccionar_Ubicacion=self.boton_Seleccionar_Ubicacion,
            entry_URL=self.entry_URL,
            entry_Ubicacion_Video=self.entry_Ubicacion_Video,
            NOMBRE_DESCARGA=NOMBRE_DESCARGA,
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
            boton_Descargar_Video=self.boton_Descargar_Video,
            boton_Descargar_Audio=self.boton_Descargar_Audio,
            boton_Seleccionar_Ubicacion=self.boton_Seleccionar_Ubicacion,
            entry_URL=self.entry_URL,
            entry_Ubicacion_Video=self.entry_Ubicacion_Video,
            NOMBRE_DESCARGA=NOMBRE_DESCARGA,
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
                Thread(
                    target=self.barraDeProgresion.AumentarProgreso(), daemon=True
                ).start()
                Thread(
                    target=self.__DescargarVideo, args=self.URL_Video, daemon=True
                ).start()
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
                Thread(target=self.barraDeProgresion.AumentarProgreso(), daemon=True)

                Thread(
                    target=self.__DescargarAudio, args=self.URL_Video, daemon=True
                ).start()
        except Exception as e:
            showerror("Error", str(e))


Main()

ventana.ActualizarVentana()
