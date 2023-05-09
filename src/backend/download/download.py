"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

from os import startfile
from typing import Callable

from flet import Page, IconButton, TextField

from control import ReadControlVariables, WriteControlVariables
from utils import LoggingManagement
from utils import check_type
from .interact_api_pytube import InteractAPIPytube


class Download:
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    @check_type
    def __init__(
        self,
        page: Page,
        change_state_widgets: Callable,
        update_progressbar: Callable,
    ):
        self.page = page
        self.change_state_widgets = change_state_widgets
        self.update_progressbar = update_progressbar

        self.interact_api_pytube = InteractAPIPytube()
        self.write_control_variables = WriteControlVariables()
        self.read_control_variables = ReadControlVariables()

    @check_type
    def download(self, download_video: bool):
        """
        Downloads a video or audio from a YouTube video and saves it to a specific location
        """

        try:
            self.update_progressbar(new_value=None, page=self.page)

            self.change_state_widgets(self.page)

            stream = self.interact_api_pytube.get_video(download_video)

            stream.download(
                output_path=self.read_control_variables.get_control_variable(
                    "VIDEO_LOCATION"
                ),
                filename=self.read_control_variables.get_control_variable(
                    "DOWNLOAD_NAME"
                ),
            )

        except Exception as exception:
            self.change_state_widgets(self.page)

            LoggingManagement.write_error(exception)

            self.update_progressbar(new_value=0, page=self.page)

            raise Exception(exception) from exception

        startfile(self.read_control_variables.get_control_variable("VIDEO_LOCATION"))

        self.update_progressbar(new_value=0, page=self.page)

        self.change_state_widgets(self.page)

        self.write_control_variables.reset()

        LoggingManagement.write_log("Download completed successfully")
