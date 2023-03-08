"""Interact with the pytube API"""
from sys import exit

from pytube import YouTube

from client.logging_management import LoggingManagement

log = LoggingManagement()


class InteractAPIPytube:
    """Interact with the pytube API"""

    def __init__(self):
        from control_variables import ControlVariables

        self.variables_control = ControlVariables()

    def get_video(self, video):
        """
        Takes a link to a YouTube video and returns the highest resolution video or audio.

        :param video: boolean, returns video if true or audio if false
        :return: The video or audio.
        """
        _video_id = YouTube(url=self.variables_control.get_url_video())
        print(_video_id)

        if video:
            self.variables_control.set_download_name(f"{_video_id.title}.mp4")
            log.write_log("The video will be downloaded")
            return _video_id.streams.get_highest_resolution()

        self.variables_control.set_download_name(f"{_video_id.title}.mp3")
        log.write_log("Audio will be downloaded")
        return _video_id.streams.get_audio_only()

    @staticmethod
    def cancel_download():
        """
        Cancel the download of the video and/or audio and then delete it
        """
        try:
            raise KeyboardInterrupt("Download canceled by user")
        except KeyboardInterrupt as exc:
            print(exc)
            print()
            log.write_error(str(exc))
        finally:
            exit()
