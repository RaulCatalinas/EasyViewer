from os import chdir
from os.path import dirname


def Ruta_Del_Archivo_De_Configuracion():
    chdir(dirname(__file__))
    return "Config.cfg"