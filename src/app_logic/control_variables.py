"""Controls the logic of control variables"""

from configparser import ConfigParser
from threading import Thread, Lock
from typing import Union

from client.app_settings import AppSettings


class ControlVariables(AppSettings):
    """Controls the logic of control variables"""

    def __init__(self):
        super().__init__()

        self.control_variables_file = self.get_file_control_variables()

        self.config = ConfigParser()

        self.config.read(self.control_variables_file, encoding="utf-8")

        self.lock = Lock()

    def set_control_variable_in_ini(
        self, control_variable: str, value: Union[str, bool]
    ):
        """Sets a new value for a control variable"""

        self.config.set(
            section="ControlVariables",
            option=control_variable.lower(),
            value=str(value),
        )

        VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

        if VIDEO_LOCATION not in ["", None]:
            self.__save_in_ini()

    def get_control_variables(
        self, control_variable: str, get_bool=False
    ) -> str | bool:
        """Gets the value of the control variable"""

        if not get_bool:
            return self.config.get(
                section="ControlVariables", option=control_variable.lower()
            )

        return self.config.getboolean(
            section="ControlVariables", option=control_variable.lower()
        )

    def __save_in_ini(self) -> None:
        """Saves the location selected by the user in the JSON file"""

        try:
            with self.lock, open(
                self.control_variables_file, mode="w", encoding="utf-8"
            ) as f:
                Thread(
                    target=self.config.write,
                    args=[f],
                    daemon=False,
                ).start()

        except Exception as exception:
            raise Exception(exception) from exception
