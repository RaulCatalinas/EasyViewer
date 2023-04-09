"""Interact with the pytube API"""

from sys import exit

from pytube import YouTube

from client.logging_management import LoggingManagement
from control_variables import ControlVariables


class InteractAPIPytube(LoggingManagement, ControlVariables):
    """Interact with the pytube API"""

    def __init__(self):
        ControlVariables.__init__(self)
        LoggingManagement.__init__(self)

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


def cancel_download():
    """
    Cancel the download of the video and/or audio and then delete it
    """
    try:
        raise KeyboardInterrupt("Download canceled by user")
    except KeyboardInterrupt as exc:
        print()
        print(exc)
    finally:
        exit()
