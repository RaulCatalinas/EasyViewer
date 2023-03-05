"""Crea la GUI del programa"""

from actualizar_dependencias import ActualizarDependencias

# Primero actualizamos las dependencias del programa
ActualizarDependencias()

# Y ahora importamos y creamos la GUI del mismo
from threading import Thread
from tkinter.messagebox import showerror
from barra_de_progresion import BarraDeProgresion
from barra_de_tareas import BarraDeTareas
from crear_botones import Boton
from crear_entrys import CrearEntrys
from crear_etiquetas import Etiqueta
from get_config import Config
from logica_app.cerrar import Cerrar
from logica_app.downloader import Descargar
from logica_app.seleccionar_directorio import SeleccionarDirectorio
from logica_app.validaciones import Validaciones
from menu_de_opciones import MenuDeOpciones
from ventana import Ventana

config = Config()
validaciones = Validaciones()

# Ventana
ventana = Ventana(
    color_fondo=config.get_config_json("COLORES", "NEGRO"),
    titulo_ventana=config.get_config_json("VENTANA", "TITULO"),
    ancho=config.get_config_json("VENTANA", "ANCHO"),
    alto=config.get_config_json("VENTANA", "ALTO"),
    icono=config.get_icono(),
)

from logica_app.variables_control import LINK_VIDEO, UBICACION_VIDEO

Cerrar(
    parent=ventana,
    color_fondo=config.get_config_json("COLORES", "NEGRO"),
    color_boton_salir_raton_dentro=config.get_config_json("COLORES", "ROJO"),
    color_boton_salir_raton_fuera=config.get_config_json("COLORES", "ROJO_OSCURO"),
    color_boton_minimizar_raton_dentro=config.get_config_json("COLORES", "NARANJA"),
    color_boton_minimizar_raton_fuera=config.get_config_json(
        "COLORES", "NARANJA_OSCURO"
    ),
    color_boton_cancelar_raton_dentro=config.get_config_json("COLORES", "AMARILLO"),
    color_boton_cancelar_raton_fuera=config.get_config_json(
        "COLORES", "AMARILLO_OSCURO"
    ),
    ancho=config.get_config_json("VENTANA_CONTROL_CIERRE", "ANCHO"),
    alto=config.get_config_json("VENTANA_CONTROL_CIERRE", "ALTO"),
    color_etiqueta=config.get_config_json("COLORES", "AZUL_ETIQUETAS"),
)

menu = MenuDeOpciones(ventana=ventana, texto_a_copiar=LINK_VIDEO)


# Clase principal del programa
class Main:
    """
    Crea la GUI para el programa.
    """

    def __init__(self):
        BarraDeTareas(
            ventana=ventana, actualizar_texto_widgets=self.__actualizar_texto_widgets
        )

        # Texto + Caja + Botón de descargar video
        self.eitiqueta_url = Etiqueta(
            texto=config.get_config_execel(numero_columna_excel=0),
            posicion_eje_y=10,
            ancho=30,
            color_fondo=config.get_config_json("COLORES", "AZUL_ETIQUETAS"),
            fuente="Helvetica",
            tamaño_fuente=18,
            ventana=ventana,
        )

        self.entry_url = CrearEntrys(
            ventana=ventana,
            textvariable=LINK_VIDEO,
            fuente="Helvetica",
            tamaño_fuente=15,
            ancho=70,
            posicion_eje_y=20,
        )

        ventana.bind("<Button-3>", menu.crear_menu_de_opciones)

        # ---------------------------------------------------------------------------

        # Texto + Caja + Botón de ubicación para guardar el video
        self.etiqueta_ubicacion_video = Etiqueta(
            texto=config.get_config_execel(numero_columna_excel=1),
            posicion_eje_y=10,
            ancho=30,
            color_fondo=config.get_config_json("COLORES", "AZUL_ETIQUETAS"),
            fuente="Helvetica",
            tamaño_fuente=18,
            ventana=ventana,
        )

        self.entry_ubicacion_video = CrearEntrys(
            ventana=ventana,
            textvariable=UBICACION_VIDEO,
            fuente="Helvetica",
            tamaño_fuente=15,
            ancho=70,
            posicion_eje_y=20,
        )

        self.boton_seleccionar_ubicacion = Boton(
            texto=config.get_config_execel(numero_columna_excel=2),
            posicion_eje_y=10,
            ancho=20,
            color_fondo=config.get_config_json("COLORES", "VERDE_OSCURO"),
            funcion=lambda: [SeleccionarDirectorio(UBICACION_VIDEO)],
            fuente="Helvetica",
            tamaño_fuente=16,
            ventana=ventana,
            color_raton_dentro=config.get_config_json("COLORES", "VERDE"),
            color_raton_fuera=config.get_config_json("COLORES", "VERDE_OSCURO"),
            posicion_absoluta=True,
        )

        self.boton_descargar_video = Boton(
            texto=config.get_config_execel(numero_columna_excel=3),
            posicion_eje_x=220,
            posicion_eje_y=322,
            ancho=15,
            color_fondo=config.get_config_json("COLORES", "AMARILLO_OSCURO"),
            funcion=lambda: [
                Thread(target=self.__descargar_video, daemon=True).start()
            ],
            fuente="Helvetica",
            tamaño_fuente=15,
            ventana=ventana,
            color_raton_dentro=config.get_config_json("COLORES", "AMARILLO"),
            color_raton_fuera=config.get_config_json("COLORES", "AMARILLO_OSCURO"),
            posicion_absoluta=False,
        )

        self.boton_descargar_audio = Boton(
            texto=config.get_config_execel(numero_columna_excel=4),
            posicion_eje_x=420,
            posicion_eje_y=322,
            ancho=15,
            color_fondo=config.get_config_json("COLORES", "AMARILLO_OSCURO"),
            funcion=lambda: [
                Thread(target=self.__descargar_audio, daemon=True).start()
            ],
            fuente="Helvetica",
            tamaño_fuente=15,
            ventana=ventana,
            color_raton_dentro=config.get_config_json("COLORES", "AMARILLO"),
            color_raton_fuera=config.get_config_json("COLORES", "AMARILLO_OSCURO"),
            posicion_absoluta=False,
        )

        # Crear la etiqueta de la barra de progresion
        self.etiqueta_prograso_descarga = Etiqueta(
            texto=config.get_config_execel(numero_columna_excel=5),
            posicion_eje_y=97,
            ancho=20,
            color_fondo=config.get_config_json("COLORES", "AZUL_ETIQUETAS"),
            fuente="Helvetica",
            tamaño_fuente=18,
            ventana=ventana,
        )

        self.barra_de_progresion = BarraDeProgresion(
            ventana=ventana,
            posicion_eje_x=13,
            posicion_eje_y=470,
        )

    def __descargar_video(self, *args, **kwargs):
        print(args)
        print()
        print(kwargs)

        try:
            if (
                validaciones.comprobar_si_se_ha_introducido_una_url(LINK_VIDEO)
                and validaciones.comprobar_si_es_url_youtube(LINK_VIDEO)
                and validaciones.comprobar_si_se_ha_seleccionado_directorio(
                    UBICACION_VIDEO,
                )
                and validaciones.comprobar_conexion_internet()
                and validaciones.comprobar_si_el_video_esta_disponible(LINK_VIDEO)
            ):
                Descargar(
                    barra_de_progresion=self.barra_de_progresion,
                    boton_descargar_video=self.boton_descargar_video,
                    boton_descargar_audio=self.boton_descargar_audio,
                    boton_seleccionar_ubicacion=self.boton_seleccionar_ubicacion,
                    entry_url=self.entry_url,
                    entry_ubicacion_video=self.entry_ubicacion_video,
                    descargar_video=True,
                )
        except Exception as e:
            showerror("Error", str(e))

    def __descargar_audio(self, *args, **kwargs):
        print(args)
        print()
        print(kwargs)

        try:
            if (
                validaciones.comprobar_si_se_ha_introducido_una_url(LINK_VIDEO)
                and validaciones.comprobar_si_es_url_youtube(LINK_VIDEO)
                and validaciones.comprobar_si_se_ha_seleccionado_directorio(
                    UBICACION_VIDEO,
                )
                and validaciones.comprobar_conexion_internet()
                and validaciones.comprobar_si_el_video_esta_disponible(LINK_VIDEO)
            ):
                Descargar(
                    barra_de_progresion=self.barra_de_progresion,
                    boton_descargar_video=self.boton_descargar_video,
                    boton_descargar_audio=self.boton_descargar_audio,
                    boton_seleccionar_ubicacion=self.boton_seleccionar_ubicacion,
                    entry_url=self.entry_url,
                    entry_ubicacion_video=self.entry_ubicacion_video,
                    descargar_video=False,
                )
        except Exception as e:
            showerror("Error", str(e))

    def __actualizar_texto_widgets(self):
        self.eitiqueta_url.config_etiqueta(
            nuevo_texto=config.get_config_execel(numero_columna_excel=0)
        )
        self.etiqueta_ubicacion_video.config_etiqueta(
            nuevo_texto=config.get_config_execel(numero_columna_excel=1)
        )
        self.boton_seleccionar_ubicacion.config_boton(
            nuevo_texto=config.get_config_execel(numero_columna_excel=2)
        )
        self.boton_descargar_video.config_boton(
            nuevo_texto=config.get_config_execel(numero_columna_excel=3)
        )
        self.boton_descargar_audio.config_boton(
            nuevo_texto=config.get_config_execel(numero_columna_excel=4)
        )
        self.etiqueta_prograso_descarga.config_etiqueta(
            nuevo_texto=config.get_config_execel(numero_columna_excel=5)
        )


Main()

ventana.actualizar_ventana()
