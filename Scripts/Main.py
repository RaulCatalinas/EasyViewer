from Scripts.BarraDeProgresion import BarraDeProgresion
from Scripts.Buscar import Buscar
from Scripts.CambiarColor import colores as color
from Scripts.CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from Scripts.CrearEntrys import CrearEntrys
from Scripts.CrearEtiquetas import Etiqueta
from Scripts.Downloader import DescargarVideo, DescargarAudio
from Scripts.Logging import GestionLogging as log
from Scripts.Menu_De_Opciones import MenuDeOpciones
from Scripts.Ventana import Ventana
from Scripts.Aumentar_Barra_De_Progresion_En_Paralelo import AumentarBarraDeProgresionEnParalelo

# -----------------------------------------------
# Ventana
ventana = Ventana()
menu = MenuDeOpciones(ventana)

from Scripts.Constantes import (
    UBICACION_VIDEO,
    LINK_VIDEO,
    PORCENTAJE_DESCARGA,
    PORCENTAJE_DESCARGA_STRING,
)


# ------------------------------------------------

# Clase principal del programa
class Main:
    def __init__(self):
        self.Etiqueta_Barra_Progress = None
        self.Boton_Descargar_Audio = None
        self.Boton_Descargar_Video = None
        self.Boton_Buscar = None
        self.Ubicacion_Video = None
        self.Ubicacion = None
        self.URL_Video = None
        self.Etiqueta_URL = None
        self.cambiarColor = None
        self.aumentarBarraDeProgreso = None
        self.descargarAudio = None
        self.descargarVideo = None
        self.buscar = None
        self.barraDeProgresion = None

    # noinspection PyArgumentList
    def FuncionMain(self):
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
        self.buscar = Buscar(UBICACION_VIDEO, log)
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
            color["azulEtiquetas"],
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
            color["azulEtiquetas"],
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
            color["verdeOscuro"],
            lambda: [self.buscar.FuncionBuscar()],
            "Helvetica",
            15,
            ventana,
            color["verdeClaro"],
            color["verdeOscuro"],
        )

        self.Boton_Descargar_Video = BotonPosicionRelativa(
            "Descargar video",
            220,
            322,
            15,
            color["amarilloOscuro"],
            lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                DescargarVideo(
                    LINK_VIDEO,
                    UBICACION_VIDEO,
                    PORCENTAJE_DESCARGA,
                    self.barraDeProgresion,
                    log,
                ),
            ],
            "Helvetica",
            15,
            ventana,
            color["amarilloClaro"],
            color["amarilloOscuro"],
        )

        self.Boton_Descargar_Audio = BotonPosicionRelativa(
            "Descargar audio",
            420,
            322,
            15,
            color["amarilloOscuro"],
            lambda: [
                self.aumentarBarraDeProgreso.FuncionAumentarBarraDeProgresionEnParalelo(),
                DescargarAudio(
                    LINK_VIDEO,
                    UBICACION_VIDEO,
                    PORCENTAJE_DESCARGA,
                    self.barraDeProgresion,
                    log,
                ),
            ],
            "Helvetica",
            15,
            ventana,
            color["amarilloClaro"],
            color["amarilloOscuro"],
        )

        # Crear la etiqueta de la barra de progresion
        self.Etiqueta_Barra_Progress = Etiqueta(
            "Progreso de la descarga:",
            97,
            20,
            color["azulEtiquetas"],
            "Helvetica",
            18,
            ventana,
        )

        # Ubicamos la barra de progresion
        self.barraDeProgresion.barraProgresionDescarga.place(x=13, y=470)

        # ---------------------------------------------------------------------------


# Crear instancia de la clase que inicia el programa
interfaz = Main()

# Llamar a la función que inicia el programa
interfaz.FuncionMain()

# Actualizar ventana
ventana.ActualizarVentana()
