from Scripts.Aumentar_Barra_De_Progresion_En_Paralelo import (
    AumentarBarraDeProgresionEnParalelo,
)
from Scripts.BarraDeProgresion import BarraDeProgresion
from Scripts.Buscar import Buscar
from Scripts.CambiarColor import Colores
from Scripts.CrearBotones import BotonPosicionAbsoluta, BotonPosicionRelativa
from Scripts.CrearEntrys import CrearEntrys
from Scripts.CrearEtiquetas import Etiqueta
from Scripts.Downloader import DescargarVideo, DescargarAudio
from Scripts.Logging import GestionLogging as log
from Scripts.Menu_De_Opciones import MenuDeOpciones
from Scripts.Ventana import Ventana

# -----------------------------------------------
# Ventana
ventana = Ventana(Colores.NEGRO.value)
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
            Colores.AMARILLO_CLARO.value,
            Colores.AMARILLO_OSCURO.value,
        )

        self.Boton_Descargar_Audio = BotonPosicionRelativa(
            "Descargar audio",
            420,
            322,
            15,
            Colores.AMARILLO_OSCURO.value,
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

        # Ubicamos la barra de progresion
        self.barraDeProgresion.barraProgresionDescarga.place(x=13, y=470)


Main()
# Actualizar ventana
ventana.ActualizarVentana()
