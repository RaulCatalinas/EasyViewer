"""Prompts the user to select a directory for the downloaded file"""

from flet import FilePicker, FilePickerResultEvent

from client.app_settings import AppSettings


class SelectDirectory(FilePicker, AppSettings):
    """Controls the logic that selects a directory for the video"""

    def __init__(self, page, confirm_dialog, input_directory):
        AppSettings.__init__(self)

        FilePicker.__init__(
            self,
            on_result=lambda event: self.__set_location(
                event=event, input_directory=input_directory, page=page
            ),
        )

        self.__add_to_page(page, confirm_dialog)

        self.get_directory_path(
            dialog_title=self.get_config_excel(13),
        )

        page.update()

    def __set_location(self, event: FilePickerResultEvent, input_directory, page):
        input_directory.value = event.path
        page.update(input_directory)

    def __add_to_page(self, page, confirm_dialog):
        return (
            page.add(self),
            page.overlay.append(self),
            page.overlay.append(confirm_dialog),
        )
