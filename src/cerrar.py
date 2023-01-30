import sys
from tkinter import Toplevel

from crear_botones import Boton
from crear_etiquetas import Etiqueta
from get_config import Config

config = Config()


class DialogoCerrar:
    """Crea un cuadro de diálogo que pregunta al usuario si desea cerrar el programa."""

    def __init__(
        self,
        parent,
        color_fondo,
        color_boton_salir_raton_dentro,
        color_boton_salir_raton_fuera,
        color_boton_minimizar_raton_dentro,
        color_boton_minimizar_raton_fuera,
        color_boton_cancelar_raton_dentro,
        color_boton_cancelar_raton_fuera,
        ancho,
        alto,
        color_etiqueta,
    ):

        self.parent = parent
        self.color_fondo = color_fondo
        self.color_boton_salir_raton_dentro = color_boton_salir_raton_dentro
        self.color_boton_salir_raton_fuera = color_boton_salir_raton_fuera
        self.color_boton_minimizar_raton_dentro = color_boton_minimizar_raton_dentro
        self.color_boton_minimizar_raton_fuera = color_boton_minimizar_raton_fuera
        self.color_boton_cancelar_raton_dentro = color_boton_cancelar_raton_dentro
        self.color_boton_cancelar_raton_fuera = color_boton_cancelar_raton_fuera
        self.ancho = ancho
        self.alto = alto
        self.color_etiqueta = color_etiqueta

        self.top = Toplevel(self.parent)
        self.top.title(config.get_config_execel(numero_columna_excel=10))

        # Cálculos para el centrado de la ventana
        ancho_ventana = self.top.winfo_screenwidth()
        alto_ventana = self.top.winfo_screenheight()

        coordenada_x = int((ancho_ventana / 2) - (ancho / 2))
        coordenada_y = int((alto_ventana / 2) - (alto / 2))

        # Redimensionar Ventana
        self.top.geometry(f"{ancho}x{alto}+{coordenada_x}+{coordenada_y}")

        self.top.configure(bg=self.color_fondo)
        self.top.resizable(False, False)

        self.etiqueta_confirmacion_cierre = Etiqueta(
            texto=config.get_config_execel(numero_columna_excel=6),
            posicion_eje_y=10,
            ancho=26,
            color_fondo=self.color_etiqueta,
            fuente="Arial",
            tamaño_fuente=12,
            ventana=self.top,
        )

        self.boton_salir = Boton(
            texto=config.get_config_execel(numero_columna_excel=7),
            posicion_eje_x=15,
            posicion_eje_y=50,
            ancho=15,
            color_fondo=self.color_boton_salir_raton_fuera,
            funcion=lambda: [self.salir()],
            fuente="Arial",
            tamaño_fuente=12,
            ventana=self.top,
            color_raton_dentro=self.color_boton_salir_raton_dentro,
            color_raton_fuera=self.color_boton_salir_raton_fuera,
            posicion_absoluta=False,
        )

        self.boton_minimizar = Boton(
            texto=config.get_config_execel(numero_columna_excel=8),
            posicion_eje_x=173,
            posicion_eje_y=50,
            ancho=15,
            color_fondo=self.color_boton_minimizar_raton_fuera,
            funcion=lambda: [self.minimizar()],
            fuente="Arial",
            tamaño_fuente=12,
            ventana=self.top,
            color_raton_dentro=self.color_boton_minimizar_raton_dentro,
            color_raton_fuera=self.color_boton_minimizar_raton_fuera,
            posicion_absoluta=False,
        )

        self.boton_cancelar = Boton(
            texto=config.get_config_execel(numero_columna_excel=9),
            posicion_eje_x=40,
            posicion_eje_y=90,
            ancho=25,
            color_fondo=self.color_boton_cancelar_raton_fuera,
            funcion=lambda: [self.cancelar()],
            fuente="Arial",
            tamaño_fuente=12,
            ventana=self.top,
            color_raton_dentro=self.color_boton_cancelar_raton_dentro,
            color_raton_fuera=self.color_boton_cancelar_raton_fuera,
            posicion_absoluta=False,
        )

    def salir(self):
        """
        Destruye la ventana superior y la ventana principal y luego sale del programa.
        """
        self.top.destroy()
        self.parent.destroy()
        sys.exit()

    def minimizar(self):
        """
        Destruye la ventana superior e iconifica la ventana principal.
        """
        self.top.destroy()
        self.parent.iconify()

    def cancelar(self):
        """
        Cierra la ventana
        """
        self.top.destroy()


class Cerrar:
    """Crea la ventana de confirmacion de cierre"""

    def __init__(
        self,
        parent,
        color_fondo,
        color_boton_salir_raton_dentro,
        color_boton_salir_raton_fuera,
        color_boton_minimizar_raton_dentro,
        color_boton_minimizar_raton_fuera,
        color_boton_cancelar_raton_dentro,
        color_boton_cancelar_raton_fuera,
        ancho,
        alto,
        color_etiqueta,
    ):

        self.dialogo = None
        self.parent = parent
        self.color_fondo = color_fondo
        self.color_boton_salir_raton_dentro = color_boton_salir_raton_dentro
        self.color_boton_salir_raton_fuera = color_boton_salir_raton_fuera
        self.color_boton_minimizar_raton_dentro = color_boton_minimizar_raton_dentro
        self.color_boton_minimizar_raton_fuera = color_boton_minimizar_raton_fuera
        self.color_boton_cancelar_raton_dentro = color_boton_cancelar_raton_dentro
        self.color_boton_cancelar_raton_fuera = color_boton_cancelar_raton_fuera
        self.ancho = ancho
        self.alto = alto
        self.color_etiqueta = color_etiqueta

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        """
        Crea una nueva ventana.
        """
        self.dialogo = DialogoCerrar(
            parent=self.parent,
            color_fondo=self.color_fondo,
            color_boton_salir_raton_dentro=self.color_boton_salir_raton_dentro,
            color_boton_salir_raton_fuera=self.color_boton_salir_raton_fuera,
            color_boton_minimizar_raton_dentro=self.color_boton_minimizar_raton_dentro,
            color_boton_minimizar_raton_fuera=self.color_boton_minimizar_raton_fuera,
            color_boton_cancelar_raton_dentro=self.color_boton_cancelar_raton_dentro,
            color_boton_cancelar_raton_fuera=self.color_boton_cancelar_raton_fuera,
            ancho=self.ancho,
            alto=self.alto,
            color_etiqueta=self.color_etiqueta,
        )

        self.parent.wait_window(self.dialogo.top)
