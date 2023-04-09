"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

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
        page,
    ):
        self.button_select_location = button_select_location
        self.button_download_video = button_download_video
        self.button_download_audio = button_download_audio
        self.input_url = input_url
        self.download_video = download_video
        self.page = page

        ControlVariables.__init__(self)
        InteractAPIPytube.__init__(self)
        LoggingManagement.__init__(self)

        self.video_location = self.get_control_variables("VIDEO_LOCATION")
        self.download_name = self.get_control_variables("DOWNLOAD_NAME")

        try:
            self.__change_state_widgets()

            self.set_control_variable_in_ini("DOWNLOADED_SUCCESSFULLY", False)

            if self.download_video:
                self.download = self.get_video(True)
            else:
                self.download = self.get_video(False)

            self.download.download(
                output_path=self.video_location,
                filename=self.download_name,
            )

        except Exception as exception:
            self.__change_state_widgets()

            self.write_error(exception)

            raise Exception(exception) from exception

        open(self.video_location)

        self.__change_state_widgets()

        self.set_control_variable_in_ini("URL_VIDEO", "")
        self.set_control_variable_in_ini("DOWNLOAD_NAME", "")
        self.set_control_variable_in_ini("DOWNLOADED_SUCCESSFULLY", True)

        self.write_log("Download completed successfully")

    def __change_state_widgets(self):
        """If the widgets are activated they deactivate it and vice versa"""

        self.button_select_location.change_state(self.page)
        self.button_download_video.change_state(self.page)
        self.button_download_audio.change_state(self.page)
        self.input_url.change_state(self.page)
