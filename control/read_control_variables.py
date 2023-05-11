"""
Reads control variables from an INI file
"""

from configparser import ConfigParser

from utils import CONFIG_FILES

ini_file_path = CONFIG_FILES["INI"]

configparser = ConfigParser()

configparser.read(ini_file_path, encoding="utf-8")


def get_control_variable(control_variable: str, get_bool: bool = False) -> str | bool:
    """
    Gets the value of the control variable

    :param control_variable: Control variable to set
    :param get_bool: If true it returns a boolean, if false it returns a str
    """

    if not get_bool:
        return configparser.get("ControlVariables", option=control_variable.lower())

    return configparser.getboolean("ControlVariables", option=control_variable.lower())
