from webbrowser import open

from client.logging_management import LoggingManagement

log = LoggingManagement()


class Download:
    """
    Downloads a video or audio from a YouTube video and saves it to a specific location
    """

    def __init__(
        self,
        progress_bar,
        button_select_location,
        video_download_button,
        audio_download_button,
        entry_url,
        entry_location_video,
        download_video,
    ):
        self.progress_bar = progress_bar
        self.button_select_location = button_select_location
        self.video_download_button = video_download_button
        self.audio_download_button = audio_download_button
        self.video_download_button = video_download_button
        self.entry_url = entry_url
        self.entry_location_video = entry_location_video
        self.download_video = download_video

        from interact_api_pytube import InteractAPIPytube
        from control_variables import ControlVariables

        self.control_variables = ControlVariables()
        self.interact_api_pytube = InteractAPIPytube()

        try:
            self.control_variables.set_downloaded_successfully(False)

            self.__disable_widgets()

            if self.download_video:
                self.download = self.interact_api_pytube.get_video(True)
            else:
                self.download = self.interact_api_pytube.get_video(False)

            self.progress_bar.execute_progression_bar()

            self.download.download(
                output_path=self.control_variables.get_location_video(),
                filename=self.control_variables.get_download_name(),
            )

        except Exception as exc:
            self.progress_bar.stop_progression_bar()

            self.__activate_widgets()

            log.write_error(str(exc))

            raise Exception(str(exc)) from exc

        variables_control.set_downloaded_successfully(True)

        open(self.control_variables.get_video_location())

        self.progress_bar.stop_progression_bar()

        self.__activate_widgets()

        log.write_log("Download completed successfully")

    def __disable_widgets(self):
        self.button_select_location.disable()
        self.video_download_button.disable()
        self.audio_download_button.disable()
        self.entry_url.disable()
        self.entry_location_video.disable()

    def __activate_widgets(self):
        self.button_select_location.activate()
        self.video_download_button.activate()
        self.audio_download_button.activate()
        self.entry_url.activate()
        self.entry_location_video.activate()
