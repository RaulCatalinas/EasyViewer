"""
Interact with the Pytube API.
"""

# Third-Party libraries
from pytubefix import YouTube

# App logging
from app_logging import LoggingManager

# App enums
from app_enums import LOG_LEVELS

# Constants
from constants import EXTENSION_FILE_VIDEO, EXTENSION_FILE_AUDIO

# Utils
from utils import clean_invalid_chars


class InteractAPIPytube:
    """
    Interact with the Pytube API.
    """

    def __init__(self):
        self.logging_manager = LoggingManager()

    def get_video(self, url: str, download_video: bool):
        """
        Get the video to download

        Args:
            url (str): URL of the video to be downloaded
            download_video (bool): Specify to download the video or only the audio

        Raises:
            Exception: Error occurred while obtaining the video

        Returns:
            pytube.Stream | None: The information of the video to download
        """

        try:
            youtube = YouTube(url)
            stream = youtube.streams

            return (
                stream.get_highest_resolution()
                if download_video
                else stream.get_audio_only()
            )

        except Exception as e:
            self.logging_manager.write_log(LOG_LEVELS.CRITICAL, str(e))

            raise Exception("Something has gone wrong try again later")

    def get_video_title(self, url: str, download_video: bool):
        """
        Returns the title of a YouTube video, with characters not allowed in OS file names removed, and with the corresponding file extension

        Args:
            url (str): URL of the video whose title you want.
            download_video (bool): Whether to use the extension '.mp4' or '.mp3'.

        Returns:
            str: The title of the video without characters not allowed in OS filenames and with the corresponding file extension.

        Example:
        >>> title = get_video_title("https://www.youtube.com/watch?v=abc123", True)
        >>> print(title)
        "My_Video_Title.mp4"

        >>> title = get_video_title("https://www.youtube.com/watch?v=xyz456", False)
        >>> print(title)
        "My_Audio_Title.mp3"
        """

        youtube = YouTube(url)
        video_title = youtube.title

        title_for_the_file = clean_invalid_chars(video_title)

        extension_file = (
            EXTENSION_FILE_VIDEO if download_video else EXTENSION_FILE_AUDIO
        )

        return f"{title_for_the_file}.{extension_file}"
