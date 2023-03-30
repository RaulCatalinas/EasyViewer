from webbrowser import open

from client.logging_management import LoggingManagement
from control_variables import ControlVariables
from interact_api_pytube import InteractAPIPytube


class Download(InteractAPIPytube, LoggingManagement, ControlVariables):
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    def __init__(
        self,
        button_select_location,
        button_download_video,
        button_download_audio,
        input_url,
        download_video,
    ):
        self.button_select_location = button_select_location
        self.button_download_video = button_download_video
        self.button_download_audio = button_download_audio
        self.input_url = input_url
        self.download_video = download_video

        ControlVariables.__init__(self)
        InteractAPIPytube.__init__(self)
        LoggingManagement.__init__(self)

        self.video_location = self.get_control_variables("VIDEO_LOCATION")
        self.download_name = self.get_control_variables("DOWNLOAD_NAME")

        try:
            print(self.video_location)

            self.set_control_variable("DOWNLOADED_SUCCESSFULLY", False)

            self.__disable_widgets()

            if self.download_video:
                self.download = self.get_video(True)
            else:
                self.download = self.get_video(False)

            self.download.download(
                output_path=self.video_location,
                filename=self.download_name,
            )

        except Exception as exc:
            self.__activate_widgets()

            self.write_error(str(exc))

            raise Exception(str(exc)) from exc

        self.set_control_variable("DOWNLOADED_SUCCESSFULLY", True)

        open(self.video_location)

        self.__activate_widgets()

        self.write_log("Download completed successfully")

    def __disable_widgets(self):
        self.button_select_location.desactivate()
        self.button_download_video.desactivate()
        self.button_download_audio.desactivate()
        self.input_url.desactivate()

    def __activate_widgets(self):
        self.button_select_location.activate()
        self.button_download_video.activate()
        self.button_download_audio.activate()
        self.input_url.activate()
