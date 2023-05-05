from configparser import ConfigParser

from utils import ConfigFiles, check_type


class ReadControlVariables(ConfigParser):
    def __init__(self):
        super().__init__()

        self.read(ConfigFiles.INI.value, encoding="utf-8")

    @classmethod
    def get(
        cls, control_variable: str, get_bool: bool = False, raw: bool = True
    ) -> str | bool:
        """
        Gets the value of the control variable

        :param control_variable: Control variable to set
        :param get_bool: If true it returns a boolean, if false it returns a str
        """

        check_type(control_variable, str)
        check_type(get_bool, bool)

        if not get_bool:
            return ConfigParser.get(
                cls(), "ControlVariables", option=control_variable.lower(), raw=raw
            )

        return ConfigParser.getboolean(
            cls(), "ControlVariables", option=control_variable.lower(), raw=raw
        )
