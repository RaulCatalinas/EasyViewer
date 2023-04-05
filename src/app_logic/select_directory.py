"""Prompts the user to select a directory for the downloaded file"""

from client.app_settings import AppSettings
from flet import FilePicker, FilePickerResultEvent

from control_variables import ControlVariables


class SelectDirectory(FilePicker, ControlVariables, AppSettings):
    """Controls the logic that selects a directory for the video"""

    def __init__(self, page, input_directory):
        self.page = page
        self.input_directory = input_directory

        ControlVariables.__init__(self)
        AppSettings.__init__(self)

        FilePicker.__init__(self, on_result=self.__on_result)

    def __on_result(self, event: FilePickerResultEvent):
        self.input_directory.value = event.path
        self.set_control_variable("VIDEO_LOCATION", event.path)
        self.page.update(self.input_directory)

    def select_directory(self):
        self.get_directory_path(
            dialog_title=self.get_config_excel(13),
        )
