"""
Save control variables in an INI file and reset their values.
"""

# Standard library
from configparser import ConfigParser
from threading import Lock, Thread

# Third-Party libraries
from flet import Page

# Osutils
from osutils import FileHandler, GetPaths

# Utils
from utils import check_type


class ControlVariables:
    """
    Save control variables in an INI file and reset their values.
    """

    def __init__(self):
        self.lock = Lock()
        self.ini_file_path = GetPaths.get_config_file("ini")

        FileHandler.check_file_exists(self.ini_file_path)

        self.config_parser = ConfigParser()
        self.config_parser.read(self.ini_file_path, encoding="utf-8")

    @check_type
    def get_control_variable(
        self, control_variable: str, get_bool: bool = False
    ) -> str | bool:
        """
        Gets the value of the control variable

        Args:
            control_variable (str): Control variable to get
            get_bool (bool, optional): Indicates whether to return a boolean or str

        Returns:
            str | bool: _description_
        """

        section = "ControlVariables"
        option = control_variable.lower()

        return (
            self.config_parser.getboolean(section, option)
            if get_bool
            else self.config_parser.get(section, option)
        )

    @check_type
    def set_control_variable(self, control_variable: str, value: str | bool):
        """
        Sets a new value for the control variable

        Args:
            control_variable (str): Control variable to set
            value (str | bool): Value to set in the control variable
        """

        section = "ControlVariables"
        option = control_variable.lower()
        value = str(value)

        self.config_parser.set(section, option, value)

        self.__save_to_ini()

    @check_type
    def __save_to_ini(self):
        """
        Saves the value of control variables in an INI file

        Raises:
            Exception: Error happened in the process
        """

        try:
            with self.lock, open(self.ini_file_path, mode="w", encoding="utf-8") as f:
                Thread(target=self.config_parser.write, args=[f], daemon=False).start()

        except Exception as exception:
            raise Exception(exception) from exception

    @check_type
    def save_to_local_storage(self, page: Page):
        """
        Saves the video location to the user's local storage.

        Args:
            page (flet.Page): Reference to the app window
        """

        video_location = self.get_control_variable("VIDEO_LOCATION")
        checkbox_update = self.get_control_variable("checkbox_update")

        page.client_storage.set("video_location", video_location)
        page.client_storage.set("checkbox_update", checkbox_update)

    @check_type
    def set_initial_values(self, page: Page):
        """
        Sets initial values for control variables

        Args:
            page (flet.Page): Reference to the app window
        """

        video_location = page.client_storage.get("video_location")
        checkbox = page.client_storage.get("checkbox_update")

        self.set_control_variable("VIDEO_LOCATION", video_location)
        self.set_control_variable("checkbox_update", checkbox)

    def reset(self):
        """
        Resets the value of the control variables
        """

        self.set_control_variable("DOWNLOAD_NAME", "")
        self.set_control_variable("URL_VIDEO", "")
