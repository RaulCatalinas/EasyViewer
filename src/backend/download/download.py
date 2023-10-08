"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

# Standard library
from os import startfile

# Control variables
from control_variables import ControlVariables

# Third-Party libraries
from flet import Page

# Utils
from utils import LoggingManagement, check_type

# Interact api pytube
from .interact_api_pytube import InteractAPIPytube


class Download:
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    @check_type
    def __init__(self, page: Page):
        self.page = page
        self.interact_api_pytube = InteractAPIPytube()
        self.control_variables = ControlVariables()

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
            stream = self.interact_api_pytube.get_video(download_video)

            stream.download(
                output_path=self.control_variables.get_control_variable(
                    "VIDEO_LOCATION"
                ),
                filename=self.control_variables.get_control_variable("DOWNLOAD_NAME"),
            )

        except Exception as exception:
            LoggingManagement.write_error(str(exception))

            raise Exception(str(exception)) from exception

        startfile(self.control_variables.get_control_variable("VIDEO_LOCATION"))

        self.control_variables.reset()

        LoggingManagement.write_log("Download completed successfully")
