"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

from os import startfile
from typing import Callable

from flet import Page

from control import get_control_variable, WriteControlVariables
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

    @check_type
    def download(self, download_video: bool):
        """
        Downloads a video or audio from a YouTube video and saves it to a specific location
        """

        try:
            self.update_progressbar(new_value=None, page=self.page)

            self.change_state_widgets(self.page)

            stream = InteractAPIPytube().get_video(download_video)

            stream.download(
                output_path=get_control_variable("VIDEO_LOCATION"),
                filename=get_control_variable("DOWNLOAD_NAME"),
            )

        except Exception as exception:
            self.change_state_widgets(self.page)

            LoggingManagement.write_error(exception)

            self.update_progressbar(new_value=0, page=self.page)

            raise Exception(exception) from exception

        startfile(get_control_variable("VIDEO_LOCATION"))

        self.update_progressbar(new_value=0, page=self.page)

        self.change_state_widgets(self.page)

        WriteControlVariables().reset()

        LoggingManagement.write_log("Download completed successfully")
