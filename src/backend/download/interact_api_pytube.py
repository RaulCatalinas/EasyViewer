"""
Interact with the Pytube API.
"""

from pytube import YouTube

from config import ExcelTextLoader
from control import ControlVariables
from osutils import FileHandler
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
        Takes a URL from a YouTube video and returns the highest resolution video or audio.

        :param url: URL of the YouTube video.

        :param download_video: If True, download the video. If it's False, download only the audio.

        :return: The video or audio.
        """

        url = self.control_variables.get_control_variable("URL_VIDEO")

        try:
            video_id = YouTube(url)
            title = video_id.title

            title_for_the_file = FileHandler.clean_invalid_chars(title)

            extension_file = "mp3" if not download_video else "mp4"
            downloaded_file_type = "audio" if not download_video else "video"

            self.control_variables.set_control_variable_in_ini(
                option="DOWNLOAD_NAME",
                value=f"{title_for_the_file}.{extension_file}",
            )

            LoggingManagement.write_log(
                f"The {downloaded_file_type} will be downloaded."
            )

            if download_video:
                return video_id.streams.get_highest_resolution()

            return video_id.streams.get_audio_only()

        except Exception as exception:
            LoggingManagement.write_error(exception)

            raise Exception(ExcelTextLoader.get_text(17)) from exception
