from enum import Enum


class Colores(Enum):
    AZUL_ETIQUETAS = "#00FFEF"
    VERDE_OSCURO = "#003300"
    VERDE_CLARO = "#00FF00"
    NEGRO = "#000000"
    AMARILLO_OSCURO = "#333300"
    AMARILLO_CLARO = "#FFFF00"


# Clase que cambia el color de los botones al pasar el ratón por encima
class CambiarColor:
    @staticmethod
    def FuncionCambiarColor(button, colorRatonDentro, colorRatonFuera):
        """
        Toma un botón y dos colores, y vincula el botón para cambiar de color cuando el mouse ingresa y deja el botón
        @param button - El botón al que desea cambiar el color.
        @param colorRatonDentro - El color del botón cuando el mouse está sobre él.
        @param colorRatonFuera - El color del botón cuando el mouse no está sobre él.
        """
        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=colorRatonDentro, cursor="hand2"),
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))
