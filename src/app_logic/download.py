"""
Downloads a video or audio from a YouTube video and saves it to a specific location
"""

from os import startfile

from client.logging_management import LoggingManagement
from interact_api_pytube import InteractAPIPytube


class Download(InteractAPIPytube, LoggingManagement):
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
        set_control_variable_in_ini,
        get_control_variables,
        change_state_widgets,
        reset_control_variables,
        update_progressbar,
    ):
        self.button_select_location = button_select_location
        self.button_download_video = button_download_video
        self.button_download_audio = button_download_audio
        self.input_url = input_url
        self.download_video = download_video
        self.page = page
        self.set_control_variable_in_ini = set_control_variable_in_ini
        self.get_control_variables = get_control_variables
        self.change_state_widgets = change_state_widgets
        self.reset_control_variables = reset_control_variables
        self.update_progressbar = update_progressbar

        InteractAPIPytube.__init__(
            self,
            set_control_variable_in_ini,
        )
        LoggingManagement.__init__(self)

        self.video_location = self.get_control_variables("VIDEO_LOCATION")
        self.download_name = self.get_control_variables("DOWNLOAD_NAME")

        try:
            self.update_progressbar(new_value=None, page=self.page)

            self.change_state_widgets(self.page)

            if self.download_video:
                self.download = self.get_video(True)
            else:
                self.download = self.get_video(False)

            self.download.download(
                output_path=self.video_location,
                filename=self.download_name,
            )

        except Exception as exception:
            self.change_state_widgets(self.page)

            self.write_error(exception)

            self.update_progressbar(new_value=0, page=self.page)

            raise Exception(exception) from exception

        startfile(self.video_location)

        self.change_state_widgets(self.page)

        self.reset_control_variables()

        self.write_log("Download completed successfully")

        self.update_progressbar(new_value=0, page=self.page)
