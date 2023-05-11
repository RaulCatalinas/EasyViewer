"""
Save control variables in an INI file and to reset their values.
"""

from configparser import ConfigParser
from threading import Thread, Lock

from flet import Page

from osutils import FileHandler, GetPaths
from utils import check_type


class ControlVariables(ConfigParser):
    """
    Save control variables in an INI file and to reset their values.
    """

    def __init__(self):
        self.lock = Lock()
        self.ini_file_path = GetPaths.get_config_file("ini")

        FileHandler.check_file_exists(self.ini_file_path)

        super().__init__()

        self.read(self.ini_file_path, encoding="utf-8")

    @check_type
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

    @check_type
    def set_control_variable_in_ini(self, option: str, value: str | bool) -> None:
        """
        Sets a new value for a control variable
        """

        self.set("ControlVariables", option.lower(), str(value))

        self.__save_in_ini()

    @check_type
    def __save_in_ini(self):
        try:
            with self.lock, open(self.ini_file_path, mode="w", encoding="utf-8") as f:
                Thread(target=self.write, args=[f], daemon=False).start()

        except Exception as exception:
            raise Exception(exception) from exception

    @check_type
    def save_to_local_storage(self, page: Page):
        """
        Saves the video location to the user's local storage.

        :param page: It's a reference to the app window
        """

        video_location = self.get_control_variable("VIDEO_LOCATION")

        page.client_storage.set("video_location", video_location)

    @check_type
    def set_initial_values(self, page: Page):
        """
        Sets the initial value of the location for the video in the INI file

        :param page: It's a reference to the app window
        """

        video_location = page.client_storage.get("video_location")

        self.set_control_variable_in_ini(option="VIDEO_LOCATION", value=video_location)

    def reset(self):
        """
        Resets the value of the control variables
        """

        self.set_control_variable_in_ini(option="DOWNLOAD_NAME", value="")
        self.set_control_variable_in_ini(option="URL_VIDEO", value="")
