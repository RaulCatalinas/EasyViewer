from pytube import YouTube

from config import GetConfigExcel
from control import ReadControlVariables, WriteControlVariables
from osutils import FileHandler
from utils import LoggingManagement, check_type


class InteractAPIPytube(LoggingManagement):
    """
    Class to interact with the Pytube API.
    """

    def __init__(self):
        super().__init__()

    @classmethod
    def get_video(cls, download_video):
        """
        Takes a URL from a YouTube video and returns the highest resolution video or audio.

        :param url: URL of the YouTube video.
        :param download_video: If True, download the video. If it is False, download only the audio.

        :return: The video or audio.
        """

        check_type(download_video, bool)

        url = ReadControlVariables.get("URL_VIDEO")

        try:
            video_id = YouTube(url)
            title = video_id.title

            title_for_the_file = FileHandler.clean_invalid_chars(title)

            if download_video:
                WriteControlVariables.set("DOWNLOAD_NAME", f"{title_for_the_file}.mp4")

                cls.write_log("The video will be downloaded.")

                return video_id.streams.get_highest_resolution()

            WriteControlVariables.set("DOWNLOAD_NAME", f"{title_for_the_file}.mp3")

            cls.write_log("The audio will be downloaded.")

            return video_id.streams.get_audio_only()

        except Exception as exception:
            cls.write_error(exception)

            raise Exception(GetConfigExcel.get_config_excel(17)) from exception
