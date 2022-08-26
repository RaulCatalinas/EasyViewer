from os import chdir
from os.path import dirname


def getLog():
    chdir(dirname(__file__))
    return "App.log"
