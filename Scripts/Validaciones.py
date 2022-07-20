from os.path import isdir


def Comprobar_Si_Se_Ha_Seleccionado_Directorio(Directorio_Descarga, log, showerror):
    """
    Comprueba si se ha seleccionado un directorio
    """

    if isdir(Directorio_Descarga.get()):
        log.writeLog(
            "Se ha seleccionado ningún directorio para guardar el video"
        )
        return True
    else:
        showerror(
            "Error de directorio",
            "No se ha seleccionado ningún directorio",
        )
        log.writeError(
            "No se ha seleccionado un directorio para guardar el video"
        )
        return False
