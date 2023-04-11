from os import environ
from os.path import join

from pytube import YouTube
from requests import get, ConnectionError, Timeout

from client.app_settings import AppSettings
from client.logging_management import LoggingManagement


class Validations(LoggingManagement, AppSettings):
    """Required validations before downloading a video"""

    def __init__(self):
        LoggingManagement.__init__(self)
        AppSettings.__init__(self)

    def check_if_a_url_has_been_entered(self, url: str) -> bool:
        """
        Check if a URL has been entered
        """

        if not url:
            self.write_error("No URL entered")
            raise ValueError(self.get_config_excel(9))

        self.write_log("A URL has been entered")
        return True

    def check_if_is_url_youtube(self, url: str) -> bool:
        """
        Check if the URL is from YouTube
        """

        if (
            "https://www.youtube.com/watch?v=" in url
            or "https://youtu.be/" in url
            or "https://www.youtube.com/shorts/" in url
        ):
            self.write_log("The URL is from YouTube")
            return True

        self.write_error("The URL is not from YouTube")
        raise ValueError(self.get_config_excel(11))

    def check_if_directory_is_selected(
        self,
        input_directory: str,
        page: object,
        video_location: str,
        set_control_variable_in_ini,
    ) -> bool:
        """
        Check if a directory is selected,
        otherwise it puts a default directory
        """

        if not video_location or video_location == "None":
            DEFAULT_DIRECTORY = join(join(environ["USERPROFILE"]), "Desktop")
            input_directory.set_value(DEFAULT_DIRECTORY)
            set_control_variable_in_ini("VIDEO_LOCATION", DEFAULT_DIRECTORY)

            self.write_log("Default directory set")
            page.update(input_directory)

        else:
            self.write_log("A directory has been selected to save the video")

        return True

    def check_internet_connection(self) -> bool:
        """
        Check if there is an internet connection
        """
        try:
            get("https://www.google.com", timeout=5)
        except (ConnectionError, Timeout) as exc:
            self.write_error("No internet connection")
            raise ConnectionError(self.get_config_excel(10)) from exc

        self.write_log("Internet connection is available")
        return True

    def check_if_the_video_is_available(self, url: str) -> bool:
        """
        Check if the video is available
        """

        try:
            YouTube(url).check_availability()
            self.write_log("The video is available")
            return True

        except Exception as exception:
            self.write_error(exception)
            raise ValueError(exception) from exception
