"""Prompts the user to select a directory for the downloaded file"""

from flet import FilePicker, FilePickerResultEvent

from client.app_settings import AppSettings
from control_variables import ControlVariables


class SelectDirectory(FilePicker, ControlVariables, AppSettings):
    """Controls the logic that selects a directory for the video"""

    def __init__(self, page, confirm_dialog, input_directory):
        self.confirm_dialog = confirm_dialog
        self.input_directory = input_directory

        ControlVariables.__init__(self)
        AppSettings.__init__(self)

        FilePicker.__init__(
            self,
            on_result=lambda event: self.__set_location(
                event=event, page=page, input_directory=input_directory
            ),
        )

        self.__add_to_page(page)

        self.get_directory_path(
            dialog_title=self.get_config_excel(13),
        )

        page.update()

    def __set_location(self, event: FilePickerResultEvent, page, input_directory):
        PATH = event.path

        input_directory.value = PATH

        self.set_control_variable("VIDEO_LOCATION", PATH)

        return page.update(input_directory)

    def __add_to_page(self, page):
        return (
            page.add(self),
            page.overlay.append(self),
            page.overlay.append(self.confirm_dialog),
        )
