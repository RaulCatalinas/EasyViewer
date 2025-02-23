"""
Prompts the user to select a directory for the downloaded file
"""

# Third-Party libraries
from flet import FilePicker, FilePickerResultEvent

# App enums
from app_enums import UserPreferencesKeys, LOG_LEVELS

# User preferences
from user_preferences import UserPreferencesManager

# Utils
from utils import get_default_download_directory

# Components
from components.widgets.inputs import Input

# Logging
from app_logging import LoggingManager


class SelectDirectoryManager(FilePicker):
    """
    Controls the logic that selects a directory for the video
    """

    def __init__(self, input_directory: Input):
        self.input_directory = input_directory
        self.user_preferences_manager = UserPreferencesManager()
        self.logging_manager = LoggingManager()

        super().__init__(on_result=self._on_result)

    def _on_result(self, event: FilePickerResultEvent):
        """
        Sets the value of the selected directory.

        Args:
            event (FilePickerResultEvent): Contains the path of the selected directory
        """

        selected_directory = event.path or get_default_download_directory()

        self.user_preferences_manager.set_preference(
            UserPreferencesKeys.DOWNLOAD_DIRECTORY, selected_directory
        )

        self.input_directory.set_value(selected_directory)

    def select_directory(self):
        """
        Selects a directory using a dialog box
        """

        try:
            self.get_directory_path(dialog_title="Select directory")

        except Exception as e:
            self.logging_manager.write_log(LOG_LEVELS.ERROR, str(e))
