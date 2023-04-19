"""
Prompts the user to select a directory for the downloaded file
"""

from flet import FilePicker, FilePickerResultEvent

from client.app_settings import AppSettings


class SelectDirectory(FilePicker, AppSettings):
    """
    Controls the logic that selects a directory for the video
    """

    def __init__(self, page, input_directory, set_control_variable_in_ini):
        self.page = page
        self.input_directory = input_directory
        self.set_control_variable_in_ini = set_control_variable_in_ini
        AppSettings.__init__(self)

        FilePicker.__init__(self, on_result=self.__on_result)

    def __on_result(self, event: FilePickerResultEvent):
        """
        Sets the value of the selected directory and updates the page with the new value.

        :param event: FilePickerResultEvent, is an event object containing the path of the selected directory

        :type event: FilePickerResultEvent
        """

        self.input_directory.set_value(event.path)
        self.set_control_variable_in_ini("VIDEO_LOCATION", event.path)
        self.page.update(self.input_directory)

    def select_directory(self):
        """
        Selects a directory using a dialog box
        """

        self.get_directory_path(dialog_title=self.get_config_excel(13))
