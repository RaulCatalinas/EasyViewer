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
        self.progression_bar = progression_bar
        self.button_select_location = button_select_location
        self.video_download_button = video_download_button
        self.audio_download_button = audio_download_button
        self.video_download_button = video_download_button
        self.entry_url = entry_url
        self.entry_location_video = entry_location_video
        self.download_video = download_video

        from interact_api_pytube import InteractAPIPytube

        self.control_variables = VariablesControl()
        self.interact_api_pytube = InteractAPIPytube()

        try:
            self.control_variables.set_downloaded_successfully(False)

            self.__disable_widgets()

            if self.download_video:
                self.download = self.interact_api_pytube.get_video(True)
            else:
                self.download = self.interact_api_pytube.get_video(False)

            self.progression_bar.execute_progression_bar()

            self.download.download(
                output_path=self.control_variables.get_location_video(),
                filename=self.control_variables.get_download_name(),
            )

        except Exception as exc:
            self.progression_bar.stop_progression_bar()

            self.__activate_widgets()

            log.write_error(str(exc))

            raise Exception(str(exc)) from exc

        variables_control.set_downloaded_successfully(True)

        open(self.control_variables.get_video_location())

        self.progression_bar.stop_progression_bar()

        self.__activate_widgets()

        log.write_log("Download completed successfully")

    def __disable_widgets(self):
        self.button_select_location.deactivate()
        self.video_download_button.deactivate()
        self.audio_download_button.disable()
        self.entry_url.deactivate()
        self.entry_location_video.deactivate()

    def __activate_widgets(self):
        self.button_select_location.activate()
        self.video_download_button.activate()
        self.audio_download_button.activate()
        self.entry_url.activate()
        self.entry_location_video.activate()
