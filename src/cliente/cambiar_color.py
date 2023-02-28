"""Efecto Hover para los botones"""


class CambiarColor:
    """Efecto Hover para los botones"""

    @staticmethod
    def hover(button, color_raton_dentro, color_raton_fuera):
        """
        Toma un botón, un color para cuando el mouse está sobre el botón y un color para cuando el mouse no está sobre el botón.

        :param button: El botón al que se aplicará el efecto de desplazamiento
        :param color_raton_dentro: El color del botón cuando el mouse está sobre él
        :param color_raton_fuera: El color del botón cuando el mouse no está sobre él
        """
        button.bind(
            "<Enter>",
            func=lambda e: button.config(background=color_raton_dentro, cursor="hand2"),
        )

        button.bind(
            "<Leave>", func=lambda e: button.config(background=color_raton_fuera)
        )
