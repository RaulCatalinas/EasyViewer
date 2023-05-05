from configparser import ConfigParser
from pathlib import Path
from threading import Thread, Lock
from typing import Union

from utils import check_type, ConfigFiles
from .read_control_variables import ReadControlVariables


class WriteControlVariables(ConfigParser):
    LOCK = Lock()

    def __init__(self):
        super().__init__()

        if not Path(ConfigFiles.INI.value).exists():
            raise FileNotFoundError(f"Config file not found at {ConfigFiles.INI.value}")

        self.read(ConfigFiles.INI.value, encoding="utf-8")

    @classmethod
    def set(cls, option: str, value: Union[str, bool]) -> None:
        """
        Sets a new value for a control variable
        """

        check_type(option, str)

        ConfigParser.set(cls(), "ControlVariables", option.lower(), str(value))

    @classmethod
    def __save_in_ini(cls):
        try:
            with cls.LOCK, open(ConfigFiles.INI.value, mode="w", encoding="utf-8") as f:
                Thread(target=ConfigParser.write, args=[cls(), f], daemon=False).start()
        except Exception as exception:
            raise Exception(exception) from exception

    @classmethod
    def save_to_local_storage(cls, page):
        """
        Saves the video location to the frontend's local storage.

        :param page: Is a reference to the app window, it's being used to access the frontend storage functionality
        """

        page.client_storage.set(
            "video_location", ReadControlVariables.get("VIDEO_LOCATION")
        )

    @classmethod
    def set_initial_values(cls, page):
        video_location = page.client_storage.get("video_location")

        cls.set("VIDEO_LOCATION", video_location)

    @classmethod
    def reset(cls):
        """
        Resets the value of the control variables
        """

        for control_variable, value in [("DOWNLOAD_NAME", ""), ("URL_VIDEO", "")]:
            cls.set(control_variable, value)
