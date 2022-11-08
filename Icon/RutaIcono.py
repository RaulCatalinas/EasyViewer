from os import chdir
from os.path import dirname


def getRutaIcono():
    chdir(dirname(__file__))
    return "icono.png"
