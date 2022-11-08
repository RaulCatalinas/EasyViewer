import json

from Config.RutaJson import getRutaJson
from Icon.RutaIcono import getRutaIcono


class Config:
    def __init__(self):
        with open(getRutaJson()) as f:
            self.config_json = json.load(f)

        print(self.config_json)

    def getConfig(self, seccion, dato):
        return self.config_json[seccion][dato]


def getIcono():
    return getRutaIcono()
