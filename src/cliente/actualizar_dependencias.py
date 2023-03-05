from pathlib import Path
from subprocess import run, CalledProcessError, PIPE, STDOUT

from get_config import Config
from logging_app import GestionLogging

config = Config()
log = GestionLogging()


class ActualizarDependencias:
    """Acctualiza las dependencias del programa"""

    def __init__(self):
        try:
            print()

            self.salida = run(
                f"pip-upgrade {Path(config.get_ruta_proyecto(), 'requirements.txt')} -p all",
                shell=True,
                stdout=PIPE,
                stderr=STDOUT,
                universal_newlines=True,
                check=True,
            )

        except CalledProcessError as error:
            log.write_error(
                f"No se han podido actualizar las dependencias por este motivo: {error.output}"
            )
            print()
            return print(
                f"No se han podido actualizar las dependencias por este motivo: {error.output}"
            )

        log.write_log(
            f"Dependencias actualizadas correctamente, confirmacion: {self.salida.stdout}"
        )
        print()
        return print(
            f"Dependencias actualizadas correctamente, confirmacion: {self.salida.stdout}"
        )
