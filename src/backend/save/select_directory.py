"""
Prompts the user to select a directory for the downloaded file
"""

# Third-Party libraries
from flet import FilePicker, FilePickerResultEvent, Page

# Control variables
from control_variables import VideoLocation

# Create widgets
from frontend.create_widgets import CreateInputs

# Settings
from settings import ExcelTextLoader

# Utils
from utils import check_type


class SelectDirectory(FilePicker):
    """
    Controls the logic that selects a directory for the video
    """

    @check_type
    def __init__(self, page: Page, input_directory: CreateInputs):
        self.page = page
        self.input_directory = input_directory

        self.video_location = VideoLocation()

        super().__init__(on_result=self.__on_result)

    @check_type
    def __on_result(self, event: FilePickerResultEvent):
        """
        Sets the value of the selected directory.

        Args:
            event (FilePickerResultEvent): Contains the path of the selected directory
        """

        path = event.path

        if path is None:
            return

        self.input_directory.set_value(path)
        self.video_location.set(path)
        self.page.update(self.input_directory)

    def select_directory(self):
        """
        Selects a directory using a dialog box
        """

        self.get_directory_path(dialog_title=ExcelTextLoader.get_text(13))
