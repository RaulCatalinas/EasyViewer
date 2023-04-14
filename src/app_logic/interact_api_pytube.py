"""Interact with the pytube API"""

from pytube import YouTube

from client.app_settings import AppSettings
from client.logging_management import LoggingManagement


class InteractAPIPytube(LoggingManagement, AppSettings):
    """Interact with the pytube API"""

    def __init__(self, set_control_variable_in_ini):
        self.set_control_variable_in_ini = set_control_variable_in_ini

        LoggingManagement.__init__(self)
        AppSettings.__init__(self)

        self.url_video = self.get_control_variables("URL_VIDEO")

    def get_video(self, video):
        """
        Takes a link to a YouTube video and returns the highest resolution video or audio.

        :param video: boolean, returns video if true or audio if false
        :return: The video or audio.
        """
        try:
            _VIDEO_ID = YouTube(url=self.url_video)
            _TITLE = _VIDEO_ID.title

            if "|" in _TITLE:
                _NEW_TITLE = _TITLE.replace("|", "-")

            the_title_has_an_end_point = _NEW_TITLE.endswith(".")

            if the_title_has_an_end_point:
                _CORRECTED_TITLE = _NEW_TITLE.rstrip(_TITLE[-1])

            _title_for_the_file = (
                _CORRECTED_TITLE if the_title_has_an_end_point else _NEW_TITLE
            )

            if video:
                self.set_control_variable_in_ini(
                    "DOWNLOAD_NAME", f"{_title_for_the_file}.mp4"
                )

                self.write_log("The video will be downloaded")
                return _VIDEO_ID.streams.get_highest_resolution()

            self.set_control_variable_in_ini(
                "DOWNLOAD_NAME", f"{_title_for_the_file}.mp3"
            )

            self.write_log("Audio will be downloaded")
            return _VIDEO_ID.streams.get_audio_only()

        except Exception as exception:
            raise Exception(self.get_config_excel(17)) from exception
