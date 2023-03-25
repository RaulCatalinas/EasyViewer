from webbrowser import open

from client.logging_management import LoggingManagement
from control_variables import ControlVariables
from interact_api_pytube import InteractAPIPytube

log = LoggingManagement()
interact_api_pytube = InteractAPIPytube()
control_variables = ControlVariables()


class Download:
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    def __init__(
        self,
        progress_bar,
        button_select_location,
        button_download_video,
        button_download_audio,
        input_url,
        download_video,
    ):
        self.progress_bar = progress_bar
        self.button_select_location = button_select_location
        self.button_download_video = button_download_video
        self.button_download_audio = button_download_audio
        self.input_url = input_url
        self.download_video = download_video

        try:
            control_variables.set_downloaded_successfully(False)

            self.__disable_widgets()

            if self.download_video:
                self.download = interact_api_pytube.get_video(True)
            else:
                self.download = interact_api_pytube.get_video(False)

            # self.progress_bar.execute_progression_bar()

            self.download.download(
                output_path=control_variables.get_location_video(),
                filename=control_variables.get_download_name(),
            )

        except Exception as exc:
            # self.progress_bar.stop_progression_bar()

            self.__activate_widgets()

            log.write_error(str(exc))

            raise Exception(str(exc)) from exc

        control_variables.set_downloaded_successfully(True)

        open(control_variables.get_video_location())

        # self.progress_bar.stop_progression_bar()

        self.__activate_widgets()

        log.write_log("Download completed successfully")

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
