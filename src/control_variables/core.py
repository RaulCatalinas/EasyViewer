"""
Save control variables in an INI file and reset their values.
"""

# Standard library
from configparser import ConfigParser
from threading import Lock, Thread
from typing import Union

# Osutils
from osutils import FileHandler, GetPaths

# Utils
from utils import check_type


class Core:
    """
    Save control variables in an INI file and reset their values.
    """

    lock = Lock()
    ini_file_path = GetPaths.get_config_file("ini")

    FileHandler.check_file_exists(ini_file_path)

    config_parser = ConfigParser()
    config_parser.read(ini_file_path, encoding="utf-8")

    @classmethod
    @check_type
    def _get_control_variable(cls, control_variable: str, get_bool: bool = False):
        """
        Gets the value of the control variable

        Args:
            control_variable (str): Control variable to get
            get_bool (bool, optional): Indicates whether to return a boolean or str

        Returns:
            str | bool | None: Value of control variable
        """

        section = "ControlVariables"
        option = control_variable.lower()

        value_of_control_variable = cls.config_parser.get(section, option)

        if value_of_control_variable == "None":
            return None

        return (
            cls.config_parser.getboolean(section, option)
            if get_bool
            else cls.config_parser.get(section, option)
        )

    @classmethod
    @check_type
    def _set_control_variable(
        cls, control_variable: str, value: Union[str, bool, None]
    ):
        """
        Sets a new value for the control variable

        Args:
            control_variable (str): Control variable to set
            value (str | bool): Value to set in the control variable
        """

        section = "ControlVariables"
        option = control_variable.lower()
        value = str(value)

        cls.config_parser.set(section, option, value)

        cls.__save_to_ini()

    @classmethod
    @check_type
    def __save_to_ini(cls):
        """
        Saves the value of control variables in an INI file

        Raises:
            Exception: Error happened in the process
        """

        try:
            with cls.lock, open(cls.ini_file_path, mode="w", encoding="utf-8") as f:
                Thread(target=cls.config_parser.write, args=[f], daemon=False).start()

        except Exception as exception:
            raise Exception(exception) from exception
