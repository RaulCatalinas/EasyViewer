"""
Reads control variables from an INI file
"""

from configparser import ConfigParser

from osutils import FileHandler, GetPaths


class ReadControlVariables(ConfigParser):
    """
    Reads control variables from an INI file
    """

    def __init__(self):
        ini_file_path = GetPaths.get_config_file("ini")

        super().__init__()

        FileHandler.check_file_exists(ini_file_path)

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
