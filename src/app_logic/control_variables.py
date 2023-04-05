"""Controls the logic of control variables"""

from json import dump, load
from threading import Thread, Lock
from typing import Union

from client.app_settings import AppSettings


class ControlVariables(AppSettings):
    """Controls the logic of control variables"""

    def __init__(self):
        super().__init__()

        self.control_variables_file = self.get_file_control_variables()
        self.lock = Lock()

        with open(self.control_variables_file, encoding="utf-8") as read_json:
            self.dict_control_variables = load(read_json)

        print(self.dict_control_variables)

    def set_control_variable(self, control_variable: str, value: Union[str, bool]):
        """Sets a new value for a control variable"""

        self.dict_control_variables[control_variable] = value
        print()
        print(self.dict_control_variables)

        VIDEO_LOCATION = self.get_control_variables("VIDEO_LOCATION")

        if VIDEO_LOCATION not in ["", None]:
            self.__save(VIDEO_LOCATION)

    def get_control_variables(self, control_variable: str) -> str | bool:
        """Gets the value of the control variable"""

        return self.dict_control_variables[control_variable]

    def __save(self, video_location: str) -> None:
        """Saves the location selected by the user in the JSON file"""

        try:
            with self.lock, open(
                self.control_variables_file, mode="w", encoding="utf-8"
            ) as set_json:
                Thread(
                    target=dump,
                    args=[
                        {
                            "VIDEO_LOCATION": video_location,
                            "DOWNLOAD_NAME": "",
                            "URL_VIDEO": "",
                            "DOWNLOADED_SUCCESSFULLY": False,
                        },
                        set_json,
                    ],
                    daemon=False,
                ).start()

        except Exception as exception:
            raise Exception(exception) from exception
