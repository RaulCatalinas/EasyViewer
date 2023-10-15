"""
Interact with the Pytube API.
"""

# Third-Party libraries
from pytube import YouTube

# Control variables
from control_variables import URLs, DownloadName

# Osutils
from osutils import FileHandler

# Settings
from settings import ExcelTextLoader

# Utils
from utils import LoggingManagement, check_type

# Constants
from constants import (
    EXTENSION_FILE_VIDEO,
    EXTENSION_FILE_AUDIO,
    DOWNLOADED_FILE_TYPE_AUDIO,
    DOWNLOADED_FILE_TYPE_VIDEO,
)


class InteractAPIPytube:
    """
    Interact with the Pytube API.
    """

    def __init__(self):
        self.urls = URLs()
        self.download_name = DownloadName()

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
            video_id = YouTube(url)
            title = video_id.title
            stream = video_id.streams

            title_for_the_file = FileHandler.clean_invalid_chars(title)

            extension_file = (
                EXTENSION_FILE_AUDIO if not download_video else EXTENSION_FILE_VIDEO
            )
            downloaded_file_type = (
                DOWNLOADED_FILE_TYPE_AUDIO
                if not download_video
                else DOWNLOADED_FILE_TYPE_VIDEO
            )

            self.download_name.set(
                f"{title_for_the_file}.{extension_file}",
            )

            LoggingManagement.write_log(
                f"The {downloaded_file_type} will be downloaded."
            )

            return (
                stream.get_highest_resolution()
                if download_video
                else stream.get_audio_only()
            )

        except Exception as exception:
            LoggingManagement.write_error(str(exception))

            raise Exception(ExcelTextLoader.get_text(29)) from exception
