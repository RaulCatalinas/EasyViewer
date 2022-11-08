from os import chdir
from os.path import dirname


def getRutaJson():
    chdir(dirname(__file__))
    return "Config.json"
