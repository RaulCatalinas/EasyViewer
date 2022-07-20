from threading import Thread


# Clase que aumenta la barra de progreso en paralelo con la descarga
class AumentarBarraDeProgresionEnParalelo:
    def __init__(
            self,
            PORCENTAJE_DESCARGA,
            log,
            barraDeProgresion,
    ):
        self.PORCENTAJE_DESCARGA = PORCENTAJE_DESCARGA
        self.log = log
        self.barraDeProgresion = barraDeProgresion
        self.aumentarProgresoEnParalelo = None

    def FuncionAumentarBarraDeProgresionEnParalelo(self):
        """
        Creamos una instancia de la barra de progreso, luego creamos un hilo que llama a la función que aumenta la barra de
        progreso
        """
        self.aumentarProgresoEnParalelo = Thread(
            target=self.barraDeProgresion.AumentarProgreso(),
            args=self.PORCENTAJE_DESCARGA,
        )

        self.aumentarProgresoEnParalelo.start()
