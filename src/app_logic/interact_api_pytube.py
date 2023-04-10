"""Interact with the pytube API"""

from pytube import YouTube

from client.logging_management import LoggingManagement


class InteractAPIPytube(LoggingManagement):
    """Interact with the pytube API"""

    def __init__(self, set_control_variable_in_ini):
        self.set_control_variable_in_ini = set_control_variable_in_ini

        super().__init__()

        self.url_video = self.get_control_variables("URL_VIDEO")

    def get_video(self, video):
        """
        Takes a link to a YouTube video and returns the highest resolution video or audio.

        :param video: boolean, returns video if true or audio if false
        :return: The video or audio.
        """
        _VIDEO_ID = YouTube(url=self.url_video)
        _TITLE = _VIDEO_ID.title

        if video:
            self.set_control_variable_in_ini("DOWNLOAD_NAME", f"{_TITLE}.mp4")

            self.write_log("The video will be downloaded")
            return _VIDEO_ID.streams.get_highest_resolution()

        self.set_control_variable_in_ini("DOWNLOAD_NAME", f"{_TITLE}.mp3")

        self.write_log("Audio will be downloaded")
        return _VIDEO_ID.streams.get_audio_only()
