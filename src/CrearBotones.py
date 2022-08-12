from tkinter import Button

from src.CambiarColor import CambiarColor as color


class BotonPosicionAbsoluta:
    def __init__(
        self,
        texto,
        y,
        ancho,
        colorFondo,
        funcion,
        fuente,
        tamañoFuente,
        ventana,
        colorRatonDentro,
        colorRatonFuera,
    ):
        """
        Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del 4
        botón
        cuando el mouse está sobre él.
        @param texto - El texto que se mostrará en el botón.
        @param y - La distancia entre el botón y el widget anterior.
        @param ancho - ancho del botón
        @param colorFondo - color de fondo
        @param funcion - La función que se ejecutará cuando se presione el botón.
        @param fuente - La fuente del texto.
        @param tamañoFuente - El tamaño de la fuente.
        @param ventana - La ventana en la que estará el botón.
        @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
        @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
        """
        # Crea el botón con los parámetros dados
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana
        self.colorRatonDentro = colorRatonDentro
        self.colorRatonFuera = colorRatonFuera
        self.funcion = funcion

        self.boton = Button(
            self.ventana,
            text=self.texto,
            bg=self.colorFondo,
            font=(self.fuente, self.tamañoFuente),
            command=self.funcion,
            width=self.ancho,
        )

        self.boton.pack(pady=self.y)

        color.FuncionCambiarColor(
            self.boton,
            self.colorRatonDentro,
            self.colorRatonFuera,
        )


class BotonPosicionRelativa:
    def __init__(
        self,
        texto,
        x,
        y,
        ancho,
        colorFondo,
        funcion,
        fuente,
        tamañoFuente,
        ventana,
        colorRatonDentro,
        colorRatonFuera,
    ):
        """
        Crea un botón con los parámetros dados y luego llama a la función “CambiarColor” para cambiar el color del
        botón
        cuando el mouse está sobre él.
        @param texto - El texto que se mostrará en el botón.
        @param x - La distancia entre el botón y el widget anterior.
        @param y - La distancia entre el botón y el widget anterior.
        @param ancho - ancho del botón
        @param colorFondo - color de fondo
        @param funcion - La función que se ejecutará cuando se presione el botón.
        @param fuente - La fuente del texto.
        @param tamañoFuente - El tamaño de la fuente.
        @param ventana - La ventana en la que estará el botón.
        @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
        @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
        """

        # Crea el botón con los parámetros dados
        self.texto = texto
        self.y = y
        self.ancho = ancho
        self.colorFondo = colorFondo
        self.fuente = fuente
        self.tamañoFuente = tamañoFuente
        self.ventana = ventana
        self.colorRatonDentro = colorRatonDentro
        self.colorRatonFuera = colorRatonFuera
        self.funcion = funcion

        self.boton = Button(
            self.ventana,
            text=self.texto,
            bg=self.colorFondo,
            font=(self.fuente, self.tamañoFuente),
            command=self.funcion,
            width=self.ancho,
        )

        self.boton.place(x=x, y=y)

        color.FuncionCambiarColor(
            self.boton,
            self.colorRatonDentro,
            self.colorRatonFuera,
        )
