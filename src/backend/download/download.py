"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

# Control variables
from control_variables import VideoLocation, DownloadName

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
        self.video_location = VideoLocation()
        self.download_name = DownloadName()

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
                output_path=self.video_location.get(),
                filename=self.download_name.get(),
            )

        except Exception as exception:
            LoggingManagement.write_error(str(exception))

            raise Exception(str(exception)) from exception
