"""
Save control variables in an INI file and to reset their values.
"""

from configparser import ConfigParser
from threading import Thread, Lock

from flet import Page

from utils import CONFIG_FILES
from .read_control_variables import get_control_variable


class WriteControlVariables(ConfigParser):
    """
    Save control variables in an INI file and to reset their values.
    """

    def __init__(self):
        self.lock = Lock()
        self.ini_file_path = CONFIG_FILES["INI"]

        super().__init__()

        self.read(self.ini_file_path, encoding="utf-8")

    def set_control_variable_in_ini(self, option: str, value: str | bool) -> None:
        """
        Sets a new value for a control variable
        """

        self.set("ControlVariables", option.lower(), str(value))

        self.__save_in_ini()

    def __save_in_ini(self):
        try:
            with self.lock, open(self.ini_file_path, mode="w", encoding="utf-8") as f:
                Thread(target=self.write, args=[f], daemon=False).start()

        except Exception as exception:
            raise Exception(exception) from exception

    def save_to_local_storage(self, page: Page):
        """
        Saves the video location to the user's local storage.

        :param page: It's a reference to the app window
        """

        video_location = get_control_variable("VIDEO_LOCATION")

        page.client_storage.set("video_location", video_location)

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
