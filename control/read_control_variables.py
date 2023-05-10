"""
Reads control variables from an INI file
"""

from configparser import ConfigParser

from utils import CONFIG_FILES


class ReadControlVariables(ConfigParser):
    """
    Reads control variables from an INI file
    """

    def __init__(self):
        ini_file_path = CONFIG_FILES["INI"]

        super().__init__()

        self.read(ini_file_path, encoding="utf-8")

    def get_control_variable(
        self, control_variable: str, get_bool: bool = False
    ) -> str | bool:
        """
        Gets the value of the control variable

        :param control_variable: Control variable to set
        :param get_bool: If true it returns a boolean, if false it returns a str
        """

        if not get_bool:
            return self.get("ControlVariables", option=control_variable.lower())

        return self.getboolean("ControlVariables", option=control_variable.lower())
