from os import chdir
from os.path import dirname


def getIcono():
    chdir(dirname(__file__))
    return "icono.png"
