from os import chdir
from os.path import dirname
from sys import exit
from tkinter import Toplevel

from CrearBotones import BotonPosicionRelativa
from CrearEtiquetas import Etiqueta
from src.Icon import Icono


class DialogoCerrar:
    def __init__(
        self,
        parent,
        colorFondo,
        color_Boton_Salir_Raton_Dentro,
        color_Boton_Salir_Raton_Fuera,
        color_Boton_Minimizar_Raton_Dentro,
        color_Boton_Minimizar_Raton_Fuera,
        ancho,
        alto,
        colorEtiqueta,
    ):
        """
        Crea una ventana Toplevel, y luego crea dos botones, uno que llama a la función salir() y el otro que llama a la
        función minimizar()
        @param parent - La ventana principal.
        @param colorFondo - El color de fondo de la ventana.
        @param color_Boton_Salir_Raton_Dentro - El color del botón salir cuando el ratón pasa por encima.
        @param color_Boton_Salir_Raton_Fuera - El color del botón salir cuando el ratón no pasa por encima.
        @param color_Boton_Minimizar_Raton_Dentro - El color del botón minimizar cuando el ratón pasa por encima.
        @param color_Boton_Minimizar_Raton_Fuera - El color del botón minimizar cuando el ratón no pasa por encima.
        """

        self.parent = parent
        self.colorFondo = colorFondo
        self.color_Boton_Salir_Raton_Dentro = color_Boton_Salir_Raton_Dentro
        self.color_Boton_Salir_Raton_Fuera = color_Boton_Salir_Raton_Fuera
        self.color_Boton_Minimizar_Raton_Dentro = color_Boton_Minimizar_Raton_Dentro
        self.color_Boton_Minimizar_Raton_Fuera = color_Boton_Minimizar_Raton_Fuera
        self.ancho = ancho
        self.alto = alto
        self.colorEtiqueta = colorEtiqueta

        self.top = Toplevel(self.parent)
        self.__CentrarVentana()
        self.top.iconbitmap(Icono.getIcono())
        chdir(dirname(__file__))
        self.top.title("Salir")
        self.top.configure(bg=self.colorFondo)
        self.top.resizable(False, False)

        Etiqueta(
            "¿Está seguro de que desea salir?",
            10,
            26,
            self.colorEtiqueta,
            "Arial",
            12,
            self.top,
        )

        BotonPosicionRelativa(
            "Si, salir de la app",
            3,
            50,
            15,
            self.color_Boton_Salir_Raton_Fuera,
            lambda: [self.salir()],
            "Arial",
            12,
            self.top,
            self.color_Boton_Salir_Raton_Dentro,
            self.color_Boton_Salir_Raton_Fuera,
        )

        BotonPosicionRelativa(
            "No, solo minimizar",
            154,
            50,
            15,
            self.color_Boton_Minimizar_Raton_Fuera,
            lambda: [self.minimizar()],
            "Arial",
            12,
            self.top,
            self.color_Boton_Minimizar_Raton_Dentro,
            self.color_Boton_Minimizar_Raton_Fuera,
        )

    def salir(self):
        self.top.destroy()
        self.parent.destroy()
        exit()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()

    def __CentrarVentana(self):
        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.top.winfo_screenwidth()
        Alto_Ventana = self.top.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (self.ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (self.alto / 2))

        # Redimensionar Ventana
        return self.top.geometry(
            "{}x{}+{}+{}".format(self.ancho, self.alto, Coordenada_X, Coordenada_Y)
        )


class Cerrar:
    def __init__(
        self,
        parent,
        colorFondo,
        color_Boton_Salir_Raton_Dentro,
        color_Boton_Salir_Raton_Fuera,
        color_Boton_Minimizar_Raton_Dentro,
        color_Boton_Minimizar_Raton_Fuera,
        ancho,
        alto,
        colorEtiqueta,
    ):
        """
        La función se llama cuando la ventana se va a cerrar.
        @param parent - El widget principal.
        @param colorFondo - El color de la ventana.
        @param color_Boton_Salir_Raton_Dentro - El color del botón salir cuando el ratón pasa por encima.
        @param color_Boton_Salir_Raton_Fuera - El color del botón salir cuando el ratón no pasa por encima.
        @param color_Boton_Minimizar_Raton_Dentro - El color del botón minimizar cuando el ratón pasa por encima.
        @param color_Boton_Minimizar_Raton_Fuera - El color del botón minimizar cuando el ratón no pasa por encima.
        """
        self.dialogo = None
        self.parent = parent
        self.colorFondo = colorFondo
        self.color_Boton_Salir_Raton_Dentro = color_Boton_Salir_Raton_Dentro
        self.color_Boton_Salir_Raton_Fuera = color_Boton_Salir_Raton_Fuera
        self.color_Boton_Minimizar_Raton_Dentro = color_Boton_Minimizar_Raton_Dentro
        self.color_Boton_Minimizar_Raton_Fuera = color_Boton_Minimizar_Raton_Fuera
        self.ancho = ancho
        self.alto = alto
        self.colorEtiqueta = colorEtiqueta

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.dialogo = DialogoCerrar(
            self.parent,
            self.colorFondo,
            self.color_Boton_Salir_Raton_Dentro,
            self.color_Boton_Salir_Raton_Fuera,
            self.color_Boton_Minimizar_Raton_Dentro,
            self.color_Boton_Minimizar_Raton_Fuera,
            self.ancho,
            self.alto,
            self.colorEtiqueta,
        )

        self.parent.wait_window(self.dialogo.top)
