from os import chdir
from os.path import dirname
from sys import exit
from tkinter import Toplevel, PhotoImage

from CrearBotones import BotonPosicionRelativa
from CrearEtiquetas import Etiqueta
from Icon.Icono import getIcono


class DialogoCerrar:
    def __init__(
        self,
        parent,
        colorFondo,
        color_Boton_Salir_Raton_Dentro,
        color_Boton_Salir_Raton_Fuera,
        color_Boton_Minimizar_Raton_Dentro,
        color_Boton_Minimizar_Raton_Fuera,
        color_Boton_Cancelar_Raton_Dentro,
        color_Boton_Cancelar_Raton_Fuera,
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
        @param color_Boton_Cancelar_Raton_Dentro - El color del botón cancelar cuando el ratón pasa por encima.
        @param color_Boton_Cancelar_Raton_Fuera - El color del botón cancelar cuando el ratón no pasa por encima.
        """

        self.parent = parent
        self.colorFondo = colorFondo
        self.color_Boton_Salir_Raton_Dentro = color_Boton_Salir_Raton_Dentro
        self.color_Boton_Salir_Raton_Fuera = color_Boton_Salir_Raton_Fuera
        self.color_Boton_Minimizar_Raton_Dentro = color_Boton_Minimizar_Raton_Dentro
        self.color_Boton_Minimizar_Raton_Fuera = color_Boton_Minimizar_Raton_Fuera
        self.color_Boton_Cancelar_Raton_Dentro = color_Boton_Cancelar_Raton_Dentro
        self.color_Boton_Cancelar_Raton_Fuera = color_Boton_Cancelar_Raton_Fuera
        self.ancho = ancho
        self.alto = alto
        self.colorEtiqueta = colorEtiqueta

        self.top = Toplevel(self.parent)
        self.top.iconphoto(False, PhotoImage(file=getIcono()))
        chdir(dirname(__file__))
        self.top.title("Salir")

        # Cálculos para el centrado de la ventana
        Ancho_Ventana = self.top.winfo_screenwidth()
        Alto_Ventana = self.top.winfo_screenheight()

        Coordenada_X = int((Ancho_Ventana / 2) - (ancho / 2))
        Coordenada_Y = int((Alto_Ventana / 2) - (alto / 2))

        # Redimensionar Ventana
        self.top.geometry("{}x{}+{}+{}".format(ancho, alto, Coordenada_X, Coordenada_Y))

        self.top.configure(bg=self.colorFondo)
        self.top.resizable(False, False)

        Etiqueta(
            texto="¿Está seguro de que desea salir?",
            y=10,
            ancho=26,
            colorFondo=self.colorEtiqueta,
            fuente="Arial",
            tamañoFuente=12,
            ventana=self.top,
        )

        BotonPosicionRelativa(
            texto="Si, salir de la app",
            x=15,
            y=50,
            ancho=15,
            colorFondo=self.color_Boton_Salir_Raton_Fuera,
            funcion=lambda: [self.salir()],
            fuente="Arial",
            tamañoFuente=12,
            ventana=self.top,
            colorRatonDentro=self.color_Boton_Salir_Raton_Dentro,
            colorRatonFuera=self.color_Boton_Salir_Raton_Fuera,
        )

        BotonPosicionRelativa(
            texto="No, solo minimizar",
            x=173,
            y=50,
            ancho=15,
            colorFondo=self.color_Boton_Minimizar_Raton_Fuera,
            funcion=lambda: [self.minimizar()],
            fuente="Arial",
            tamañoFuente=12,
            ventana=self.top,
            colorRatonDentro=self.color_Boton_Minimizar_Raton_Dentro,
            colorRatonFuera=self.color_Boton_Minimizar_Raton_Fuera,
        )

        BotonPosicionRelativa(
            texto="Cancelar, permanecer en la app",
            x=40,
            y=90,
            ancho=25,
            colorFondo=self.color_Boton_Cancelar_Raton_Fuera,
            funcion=lambda: [self.cancelar()],
            fuente="Arial",
            tamañoFuente=12,
            ventana=self.top,
            colorRatonDentro=self.color_Boton_Cancelar_Raton_Dentro,
            colorRatonFuera=self.color_Boton_Cancelar_Raton_Fuera,
        )

    def salir(self):
        self.top.destroy()
        self.parent.destroy()
        exit()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()

    def cancelar(self):
        self.top.destroy()


class Cerrar:
    def __init__(
        self,
        parent,
        colorFondo,
        color_Boton_Salir_Raton_Dentro,
        color_Boton_Salir_Raton_Fuera,
        color_Boton_Minimizar_Raton_Dentro,
        color_Boton_Minimizar_Raton_Fuera,
        color_Boton_Cancelar_Raton_Dentro,
        color_Boton_Cancelar_Raton_Fuera,
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
        @param color_Boton_Cancelar_Raton_Dentro - El color del botón cancelar cuando el ratón pasa por encima.
        @param color_Boton_Cancelar_Raton_Fuera - El color del botón cancelar cuando el ratón no pasa por encima.
        """
        self.dialogo = None
        self.parent = parent
        self.colorFondo = colorFondo
        self.color_Boton_Salir_Raton_Dentro = color_Boton_Salir_Raton_Dentro
        self.color_Boton_Salir_Raton_Fuera = color_Boton_Salir_Raton_Fuera
        self.color_Boton_Minimizar_Raton_Dentro = color_Boton_Minimizar_Raton_Dentro
        self.color_Boton_Minimizar_Raton_Fuera = color_Boton_Minimizar_Raton_Fuera
        self.color_Boton_Cancelar_Raton_Dentro = color_Boton_Cancelar_Raton_Dentro
        self.color_Boton_Cancelar_Raton_Fuera = color_Boton_Cancelar_Raton_Fuera
        self.ancho = ancho
        self.alto = alto
        self.colorEtiqueta = colorEtiqueta

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.dialogo = DialogoCerrar(
            parent=self.parent,
            colorFondo=self.colorFondo,
            color_Boton_Salir_Raton_Dentro=self.color_Boton_Salir_Raton_Dentro,
            color_Boton_Salir_Raton_Fuera=self.color_Boton_Salir_Raton_Fuera,
            color_Boton_Minimizar_Raton_Dentro=self.color_Boton_Minimizar_Raton_Dentro,
            color_Boton_Minimizar_Raton_Fuera=self.color_Boton_Minimizar_Raton_Fuera,
            color_Boton_Cancelar_Raton_Dentro=self.color_Boton_Cancelar_Raton_Dentro,
            color_Boton_Cancelar_Raton_Fuera=self.color_Boton_Cancelar_Raton_Fuera,
            ancho=self.ancho,
            alto=self.alto,
            colorEtiqueta=self.colorEtiqueta,
        )

        self.parent.wait_window(self.dialogo.top)
