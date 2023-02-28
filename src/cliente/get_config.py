"""Establece la configuracion de la app"""

from json import load
from os import environ
from pathlib import Path

from dotenv import load_dotenv, set_key
from pandas import read_excel

_ruta_proyecto = Path(__file__).parent.parent.parent
_ruta_json = Path(_ruta_proyecto, "config", "config.json")
_ruta_icono = Path(_ruta_proyecto, "icono", "icono.png")
_ruta_archivo_idiomas = Path(_ruta_proyecto, "config", "idiomas.xlsx")
_ruta_variables_entorno = Path(_ruta_proyecto, "config", ".env")
print(
    f"""
    {_ruta_proyecto = }
    {_ruta_json = }
    {_ruta_icono = }
    {_ruta_archivo_idiomas = }
    """
)

idiomas = read_excel(_ruta_archivo_idiomas)
print(idiomas)
print()

load_dotenv(_ruta_variables_entorno)


class Config:
    """Lee un archivo JSON y un archivo Excel, y devuelve el valor de una clave para poder configurar la app"""

    def __init__(self):
        with open(_ruta_json, encoding="utf-8") as json:
            self.config_json = load(json)

        print(self.config_json)

    def get_config_json(self, seccion, dato):
        """
        Devuelve el valor de una clave en un diccionario, que está dentro de otro diccionario

        :param seccion: es la sección del archivo json
        :param dato: es el nombre del parámetro que desea obtener del archivo json
        :return: El valor de la clave "dato" en la sección "seccion" del archivo json.
        """
        return self.config_json[seccion][dato]

    def get_config_execel(self, numero_columna_excel):
        """
        Devuelve el valor de la celda en la columna del archivo excel que corresponde al idioma que el
        usuario ha seleccionado

        :param numero_columna_excel: El número de la columna en el archivo de Excel
        :return: El valor de la celda en la columna del idioma que se está utilizando.
        """
        print(idiomas.loc[numero_columna_excel][self.__get_idioma()])

        return idiomas.loc[numero_columna_excel][self.__get_idioma()]

    def set_idioma(self, idioma):
        """
        Establece el valor de la variable IDIOMA en las variables de entorno del sistema

        :param idioma: El idioma a configurar
        """
        # Almacenar idioma seleccionado de forma temporal
        environ["IDIOMA"] = idioma

        # Guardar el idioma seleccionado en la variable de entorno
        set_key(_ruta_variables_entorno, key_to_set="IDIOMA", value_to_set=idioma)

    def __get_idioma(self):
        print()
        print(f'Idioma de la app: {environ.get("IDIOMA")}')
        print()
        return environ.get("IDIOMA")


def get_icono():
    """
    Devuelve la ruta del icono.
    :return: La ruta del icono.
    """
    return _ruta_icono
