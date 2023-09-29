"""
Interact with the Pytube API.
"""

# Third-Party libraries
from pytube import YouTube

# Control variables
from control_variables import ControlVariables

# Osutils
from osutils import FileHandler

# Settings
from settings import ExcelTextLoader

# Utils
from utils import LoggingManagement, check_type


class InteractAPIPytube:
    """
    Interact with the Pytube API.
    """

    def __init__(self):
        self.control_variables = ControlVariables()

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

        url = self.control_variables.get_control_variable("URL_VIDEO")

        try:
            video_id = YouTube(url)
            title = video_id.title
            stream = video_id.streams

            title_for_the_file = FileHandler.clean_invalid_chars(title)

            extension_file = "mp3" if not download_video else "mp4"
            downloaded_file_type = "audio" if not download_video else "video"

            self.control_variables.set_control_variable(
                control_variable="DOWNLOAD_NAME",
                value=f"{title_for_the_file}.{extension_file}",
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
