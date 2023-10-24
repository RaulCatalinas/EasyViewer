"""
Interact with the Pytube API.
"""

# Third-Party libraries
from pytube import YouTube

# Control variables
from control_variables import URLs

# Settings
from settings import ExcelTextLoader

# Utils
from utils import LoggingManagement, check_type


class InteractAPIPytube:
    """
    Interact with the Pytube API.
    """

    def __init__(self):
        self.urls = URLs()

    @check_type
    def get_video(self, download_video: bool):
        """
        Get the video to download

        Args:
            download_video (bool): Specify to download the video or only the audio

        Raises:
            Exception: Error occurred while obtaining the video

        Returns:
            pytube.Stream | None: The information of the video to download
        """

        url = self.urls.get()

        try:
            if url is None:
                return

            youtube = YouTube(url)
            stream = youtube.streams

            return (
                stream.get_highest_resolution()
                if download_video
                else stream.get_audio_only()
            )

        except Exception as exception:
            LoggingManagement.write_error(str(exception))

            raise Exception(ExcelTextLoader.get_text(29)) from exception
