"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

# Standard library
from os import startfile
from typing import Callable

# Control variables
from control_variables import ControlVariables

# Third-Party libraries
from flet import Page

# Settings
# Utils
from utils import LoggingManagement, check_type

# Interact api pytube
from .interact_api_pytube import InteractAPIPytube


class Download:
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    @check_type
    def __init__(
        self,
        page: Page,
        toggle_state_widgets: Callable,
        update_progressbar: Callable,
    ):
        self.page = page
        self.toggle_state_widgets = toggle_state_widgets
        self.update_progressbar = update_progressbar

    @check_type
    def download(self, download_video: bool):
        """
        Downloads a video or audio from a YouTube video

        Args:
            download_video (bool): Specify to download the video or only the audio

        Raises:
            Exception: Error occurred during download
        """

        try:
            self.update_progressbar(new_value=None, page=self.page)

            self.toggle_state_widgets(self.page)

            stream = InteractAPIPytube().get_video(download_video)

            stream.download(
                output_path=ControlVariables().get_control_variable("VIDEO_LOCATION"),
                filename=ControlVariables().get_control_variable("DOWNLOAD_NAME"),
            )

        except Exception as exception:
            LoggingManagement.write_error(str(exception))

            self.toggle_state_widgets(self.page)

            self.update_progressbar(new_value=0, page=self.page)

            raise Exception(str(exception)) from exception

        startfile(ControlVariables().get_control_variable("VIDEO_LOCATION"))

        self.update_progressbar(new_value=0, page=self.page)

        self.toggle_state_widgets(self.page)

        ControlVariables().reset()

        LoggingManagement.write_log("Download completed successfully")
